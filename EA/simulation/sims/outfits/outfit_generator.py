from sims.outfits.outfit_utils import OutfitGeneratorRandomizationMixin
class OutfitGenerator(OutfitGeneratorRandomizationMixin, HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'tags': TunableSet(description='\n            The set of tags used to generate the outfit. Parts must match the\n            specified tag in order to be valid for the generated outfit.\n            ', tunable=TunableEnumWithFilter(tunable_type=Tag, filter_prefixes=('Uniform', 'OutfitCategory', 'Style', 'Situation'), default=Tag.INVALID, invalid_enums=(Tag.INVALID,), pack_safe=True))}

    def __call__(self, *args, **kwargs):
        self._generate_outfit(*args, tag_list=self.tags, **kwargs)
