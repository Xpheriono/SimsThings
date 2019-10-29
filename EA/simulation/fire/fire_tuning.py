from sims4.tuning.tunable import TunableEnumWithFilter
class FireTuning:
    FLAMMABLE_TAG = TunableEnumWithFilter(description='\n        Define a tag that is automatically added to all objects that are\n        flammable.\n        ', tunable_type=Tag, default=Tag.INVALID, invalid_enums=(Tag.INVALID,), filter_prefixes=('Fire',))
