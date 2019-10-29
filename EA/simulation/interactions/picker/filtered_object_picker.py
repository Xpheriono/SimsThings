from interactions.base.picker_interaction import ObjectPickerInteraction
class FilteredObjectPickerInteraction(ObjectPickerInteraction):
    ON_LOT_ONLY = 'on_lot'
    OFF_LOT_ONLY = 'off_lot'
    ANYWHERE = 'anywhere'
    INSTANCE_TUNABLES = {'object_filter': ObjectDefinitonsOrTagsVariant(description='\n            Filter to use to find an object.\n            ', tuning_group=GroupNames.PICKERTUNING), 'on_off_lot_requirement': TunableVariant(description='\n            Whether to accept objects on the active lot.\n            ', default=ON_LOT_ONLY, locked_args={ANYWHERE: ANYWHERE, OFF_LOT_ONLY: OFF_LOT_ONLY, ON_LOT_ONLY: ON_LOT_ONLY}, tuning_group=GroupNames.PICKERTUNING)}

    @flexmethod
    def _get_objects_gen(cls, inst, target, context, **kwargs):
        object_manager = services.object_manager()
        if cls.on_off_lot_requirement == cls.ANYWHERE:
            yield from object_manager.get_objects_with_filter_gen(cls.object_filter)
        elif cls.on_off_lot_requirement == cls.ON_LOT_ONLY:
            for obj in object_manager.get_objects_with_filter_gen(cls.object_filter):
                if obj.is_on_active_lot():
                    yield obj
        else:
            for obj in object_manager.get_objects_with_filter_gen(cls.object_filter):
                if not obj.is_on_active_lot():
                    yield obj
