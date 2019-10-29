from objects.gardening.gardening_component_fruit import GardeningFruitComponent
class TunableGardeningComponentVariant(TunableVariant):

    def __init__(self, **kwargs):
        super().__init__(fruit_component=GardeningFruitComponent.TunableFactory(), plant_component=GardeningPlantComponent.TunableFactory(), shoot=GardeningShootComponent.TunableFactory(), locked_args={'disabled': None}, default='disabled', **kwargs)
