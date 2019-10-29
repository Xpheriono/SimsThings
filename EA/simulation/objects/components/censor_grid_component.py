from collections import namedtuple
class CensorState(enum.Int):
    OFF = 3188902525
    TORSO = 3465735571
    TORSO_PELVIS = 2022575029
    PELVIS = 2484305261
    TODDLER_PELVIS = 1215676254
    FULLBODY = 958941257
    RHAND = 90812611
    LHAND = 2198569869

class CensorGridComponent(Component, component_name=types.CENSOR_GRID_COMPONENT):

    def __init__(self, owner):
        super().__init__(owner)
        self._censor_grid_handles = collections.defaultdict(list)
        self._censor_state = CensorState.OFF
        self._get_next_handle = UniqueIdGenerator()

    def add_censor(self, state):
        handle = self._get_next_handle()
        self._censor_grid_handles[handle] = state
        self._update_censor_state()
        return handle

    def remove_censor(self, handle):
        self._censor_grid_handles.pop(handle)
        self._update_censor_state()

    def _update_censor_state(self):
        new_state = self._censor_state
        handle_values = set(self._censor_grid_handles.values())
        for rule in CENSOR_LOOKUP:
            if rule.test.issubset(handle_values):
                new_state = rule.result
                break
        if new_state != self._censor_state:
            self.owner.censor_state = new_state
            self._censor_state = new_state

class TunableCensorGridComponent(TunableFactory):
    FACTORY_TYPE = CensorGridComponent

    def __init__(self, description='Manages censor grid handles on an object.', **kwargs):
        super().__init__(description=description, **kwargs)
