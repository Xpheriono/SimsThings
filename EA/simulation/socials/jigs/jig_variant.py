from sims4.tuning.tunable import TunableVariant
class TunableJigVariant(TunableVariant):

    def __init__(self, **kwargs):
        super().__init__(definition=SocialJigFromDefinition.TunableFactory(), explicit=SocialJigExplicit.TunableFactory(), legacy=SocialJigLegacy.TunableFactory(), animation=SocialJigAnimation.TunableFactory(), default='definition', **kwargs)
