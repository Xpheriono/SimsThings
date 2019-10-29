import enum
class GameEffectType(enum.Int, export=False):
    AFFORDANCE_MODIFIER = 0
    EFFECTIVE_SKILL_MODIFIER = 1
    CONTINUOUS_STATISTIC_MODIFIER = 3
    RELATIONSHIP_TRACK_DECAY_LOCKER = 4
    MOOD_EFFECT_MODIFIER = 5
    STATISTIC_STATIC_MODIFIER = 6
    AUTONOMY_MODIFIER = 7
    WHIM_MODIFIER = 8
    PIE_MENU_MODIFIER = 9
