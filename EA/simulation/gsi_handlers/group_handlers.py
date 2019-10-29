from gsi_handlers.gameplay_archiver import GameplayArchiver
    sub_schema.add_field('sim_id', label='Sim ID', width=0.35)
    sub_schema.add_field('sim_name', label='Sim Name', width=0.4)
    sub_schema.add_field('registered_si', label='Registered SIs')
    sub_schema.add_field('social_context', label='Social Context')
    sub_schema.add_field('state', label='State', width=1)
    sub_schema.add_field('value', label='Value', width=1)
    sub_schema.add_field('constraint_description', label='Key', width=1)
    sub_schema.add_field('constraint_data', label='Value', width=1)
    cheat.add_token_param('sim_id')
    cheat.add_token_param('sim_id')
    cheat.add_token_param('sim_id')
@GsiHandler('social_groups', group_schema)
def generate_group_data():
    group_data = []
    for group in services.social_group_manager().values():
        entry = {'type': repr(group), 'count': len(group), 'shutting_down': 'x' if group.has_been_shutdown else '', 'anchor': str(getattr(group, '_anchor', None))}
        state_info = []
        entry['states'] = state_info
        if group.state_component is not None:
            for (state, value) in group.state_component.items():
                state_entry = {'state': str(state), 'value': str(value)}
                state_info.append(state_entry)
        members_info = []
        entry['group_members'] = members_info
        for sim in group:
            interactions = group._si_registry.get(sim)
            group_members_entry = {'sim_id': str(sim.id), 'sim_name': sim.full_name, 'registered_si': str(interactions), 'social_context': str(sim.get_social_context())}
            members_info.append(group_members_entry)
        constraint_info = []
        constraint_info.append({'constraint_description': 'Constraint', 'constraint_data': str(group._constraint)})
        geometry = [str(constraint.geometry) for constraint in group._constraint]
        constraint_info.append({'constraint_description': 'Constraint Geometry', 'constraint_data': ','.join(geometry)})
        entry['constraints'] = constraint_info
        group_data.append(entry)
    return group_data

    sub_schema.add_field('sim_id', label='Sim ID', width=0.35)
    sub_schema.add_field('sim_name', label='Sim Name', width=0.4)
    sub_schema.add_field('registered_si', label='Registered SIs')
    sub_schema.add_field('social_context', label='Social Context')
def archive_group_message(group, add, shutdown):
    entry = {'id': group.id, 'type': repr(group), 'count': len(group), 'add/remove': add, 'shut_down': 'x' if shutdown else ''}
    members_info = []
    entry['group_members'] = members_info
    for sim in group:
        interactions = group._si_registry.get(sim)
        group_members_entry = {'sim_id': str(sim.id), 'sim_name': sim.full_name, 'registered_si': str(interactions), 'social_context': str(sim.get_social_context())}
        members_info.append(group_members_entry)
    group_log_archiver.archive(data=entry)
