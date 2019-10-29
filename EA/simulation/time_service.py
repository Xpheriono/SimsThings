import cachesimport date_and_timeimport schedulingimport scheduling_debuggerimport servicesimport sims4.logimport sims4.service_managerimport sims4.tuning.tunablelogger = sims4.log.Logger('TimeService')
class TimeService(sims4.service_manager.Service):
    MAX_TIME_SLICE_MILLISECONDS = sims4.tuning.tunable.OptionalTunable(description='\n        If enabled, script-side time slicing will be enabled and the provided\n        tuning will be the maximum time allowed in milliseconds.\n        ', tunable=sims4.tuning.tunable.Tunable(description='\n            The maximum alloted time for the script-side time slice in milliseconds.\n            ', tunable_type=int, default=50))

    def __init__(self):
        super().__init__()
        self.sim_timeline = None
        self.wall_clock_timeline = None

    def start(self):
        sim_debugger = None
        self.sim_timeline = scheduling.Timeline(services.game_clock_service().now(), exception_reporter=self._on_exception, debugger=sim_debugger)
        self.wall_clock_timeline = scheduling.Timeline(services.server_clock_service().now(), exception_reporter=self._on_exception)
        self.sim_timeline.on_time_advanced.append(caches.clear_all_caches)

    def on_teardown(self, is_travel):
        frozen_timeline = FrozenTimeline(self.sim_timeline)
        if is_travel:

            def cross_zone_alarm(handle):
                e = handle.element
                if hasattr(e, 'cross_zone'):
                    return e.cross_zone()
                return False

            self.sim_timeline.filter_handles(cross_zone_alarm)
        else:
            self.sim_timeline.teardown()
        self.sim_timeline = frozen_timeline

    def on_zone_startup(self):
        if isinstance(self.sim_timeline, FrozenTimeline):
            frozen_timeline = self.sim_timeline
            self.sim_timeline = frozen_timeline.get_original_timeline()
            self.sim_timeline.future = self.sim_timeline.now
            services.game_clock_service().set_initial_ticks_for_zone_startup(self.sim_timeline.now.absolute_ticks())

    def stop(self):
        self.wall_clock_timeline.teardown()
        self.wall_clock_timeline = None

    def update(self, time_slice=True):
        max_time_ms = self.MAX_TIME_SLICE_MILLISECONDS if time_slice else None
        result = self.sim_timeline.simulate(services.game_clock_service().now(), max_time_ms=max_time_ms)
        if not result:
            logger.debug('Did not finish processing Sim Timeline. Current element: {}', self.sim_timeline.heap[0])
        result = self.wall_clock_timeline.simulate(services.server_clock_service().now())
        if not result:
            logger.error('Too many iterations processing wall-clock Timeline. Likely culprit: {}', self.wall_clock_timeline.heap[0])

    @property
    def sim_now(self):
        if self.sim_timeline is None:
            logger.callstack('Sim Time is being accessed while not alive.', level=sims4.log.LEVEL_ERROR)
            return date_and_time.DATE_AND_TIME_ZERO
        return self.sim_timeline.now

    @property
    def sim_future(self):
        if self.sim_timeline is None:
            logger.callstack('Sim Future Time is being accessed while not alive.', level=sims4.log.LEVEL_ERROR)
            return date_and_time.DATE_AND_TIME_ZERO
        return self.sim_timeline.future

    def is_day_time(self, time=None):
        region_instance = services.current_region()
        if region_instance is None:
            return False
        else:
            if time is None:
                time = self.sim_now
            if time.time_between_day_times(region_instance.get_sunrise_time(), region_instance.get_sunset_time()):
                return True
        return False

    def is_sun_out(self):
        region_instance = services.current_region()
        if region_instance is None or not region_instance.provides_sunlight:
            return False
        weather_service = services.weather_service()
        if weather_service is not None and weather_service.is_shady():
            return False
        return self.is_day_time()

    def is_in_sunlight(self, sim):
        return self.is_sun_out() and (sim.is_outside and not sim.is_in_shade)

    def _on_exception(self, timeline, element, exception, message):
        if timeline is self.sim_timeline:
            name = 'Sim Timeline'
        elif timeline is self.wall_clock_timeline:
            name = 'Wall clock Timeline'
        else:
            name = 'Unknown timeline'
        logger.exception('Exception in {}: {}', name, message, exc=exception, log_current_callstack=False)
        logger.callstack('The enclosing callstack follows', level=sims4.log.LEVEL_ERROR, trigger_gsi_dump=False)

    def set_max_time_slice(self, time_slice_in_milliseconds):
        self.MAX_TIME_SLICE_MILLISECONDS = time_slice_in_milliseconds

class FrozenTimeline:

    def __init__(self, original_timeline):
        self._now = original_timeline.now
        self._original_timeline = original_timeline

    @property
    def now(self):
        return self._now

    def get_original_timeline(self):
        return self._original_timeline

    def get_sub_timeline(self):
        pass

    def get_current_element(self):
        pass

@sims4.commands.Command('time_service.set_max_time_slice', command_type=sims4.commands.CommandType.Automation)
def set_max_time_slice_command(time_slice:float, _connection=None):
    time_service = services.time_service()
    if time_slice <= 0:
        sims4.commands.output('Passed a time slice that is 0 or less. Turning time slicing off.', _connection)
        time_service.set_max_time_slice(None)
    else:
        time_service.set_max_time_slice(time_slice)
