from sims4.gsi.dispatcher import GsiHandler
def get_presets():
    instance_manager = services.get_instance_manager(sims4.resources.Types.LOT_DECORATION_PRESET)
    if instance_manager.all_instances_loaded:
        return [cls.__name__ for cls in instance_manager.types.values()]
    return []

    apply_neighborhood_decorations.add_token_param('preset', dynamic_token_fn=get_presets)
    apply_zone_decorations.add_token_param('preset', dynamic_token_fn=get_presets)
    apply_zone_decorations.add_token_param('zone_id')
    sub_schema.add_field('deco_location', label='Location')
    sub_schema.add_field('decoration', label='Decoration')
@GsiHandler('decoratable_lots_view', decoratable_lots_schema)
def generate_decoratable_lots_view():
    lot_decoration_service = services.lot_decoration_service()
    if lot_decoration_service is None:
        return []
    return lot_decoration_service.get_lot_decorations_gsi_data()
