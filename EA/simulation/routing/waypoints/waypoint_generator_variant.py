from routing.waypoints.waypoint_generator_ellipse import _WaypointGeneratorEllipse
class TunableWaypointGeneratorVariant(TunableVariant):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, description='\n            Define how the waypoints are generated.\n            ', spawn_points=_WaypointGeneratorSpawnPoints.TunableFactory(), lot_points=_WaypointGeneratorLotPoints.TunableFactory(), pool_laps=_WaypointGeneratorPool.TunableFactory(), object_points=_WaypointGeneratorObjectPoints.TunableFactory(), pacing=_WaypointGeneratorPacing.TunableFactory(), multiple_objects_by_tag=_WaypointGeneratorMultipleObjectByTag.TunableFactory(), ellipse=_WaypointGeneratorEllipse.TunableFactory(), footprint=_WaypointGeneratorFootprint.TunableFactory(), unobstructed_line=_WaypointGeneratorUnobstructedLine.TunableFactory(), default='spawn_points', **kwargs)
