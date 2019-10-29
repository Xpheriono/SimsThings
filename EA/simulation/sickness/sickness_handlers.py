from event_testing.resolver import SingleSimResolver
    remove_sickness_cheat.add_token_param('sim_id')
    update_diagnosis_cheat.add_token_param('sim_id')
    clear_diagnosis_cheat.add_token_param('sim_id')
    sub_schema.add_field('symptom', label='Symptom')
    sub_schema.add_field('is_discovered', label='Discovered?')
    sub_schema.add_field('interaction', label='Interaction')
    sub_schema.add_field('interaction', label='Interaction')
    sub_schema.add_field('interaction', label='Interaction')
@GsiHandler('sick_sim_schema_view', sick_sim_schema)
def generate_sick_sim_view():
    sim_data = []
    for sim_info in tuple(services.sim_info_manager().values()):
        if sim_info.sickness_tracker is None:
            pass
        elif not sim_info.has_sickness_tracking():
            pass
        else:
            sickness = sim_info.current_sickness
            exams_performed = sim_info.sickness_tracker.exams_performed
            treatments_performed = sim_info.sickness_tracker.treatments_performed
            ruled_out_treatments = sim_info.sickness_tracker.ruled_out_treatments
            sim_data.append({'sim_id': str(hex(sim_info.id)), 'sim': sim_info.full_name, 'sickness': str(sickness), 'last_recorded_progress': str(sim_info.sickness_tracker.last_progress), 'discovered': str(sim_info.sickness_tracker.has_discovered_sickness), 'Symptoms': [{'symptom': str(symptom), 'is_discovered': str(sim_info.was_symptom_discovered(symptom))} for symptom in sickness.symptoms], 'Examinations Performed': [{'interaction': str(interaction)} for interaction in exams_performed], 'Treatments Performed': [{'interaction': str(interaction)} for interaction in treatments_performed], 'Treatments Ruled Out': [{'interaction': str(interaction)} for interaction in ruled_out_treatments]})
    return sim_data

    make_sick_cheat.add_token_param('sim_id')
    sub_schema.add_field('sickness', label='Sickness')
    sub_schema.add_field('weight', label='Weight', visualizer=GsiFieldVisualizers.INT)
    sub_schema.add_field('chance', label='Chance', visualizer=GsiFieldVisualizers.FLOAT)
    sub_schema.add_field('interaction', label='Interaction')
@GsiHandler('non_sick_sim_schema_view', non_sick_schema)
def generate_non_sick_sim_view():
    sim_data = []
    sickness_service = services.get_sickness_service()
    for sim_info in tuple(services.sim_info_manager().values()):
        if sim_info.sickness_tracker is None:
            pass
        else:
            resolver = SingleSimResolver(sim_info)
            if not sim_info.is_sick():
                if not sickness_service.can_become_sick(resolver):
                    pass
                else:
                    weighted_sicknesses = tuple(all_sickness_weights_gen(resolver))
                    total_weight = float(sum(item[0] for item in weighted_sicknesses))
                    if not total_weight:
                        pass
                    else:
                        exams_performed = sim_info.sickness_tracker.exams_performed
                        sickness_data = []
                        for item in weighted_sicknesses:
                            sickness_data.append({'sickness': str(item[1]), 'weight': item[0], 'chance': item[0]/total_weight})
                        sim_data.append({'sim_id': str(hex(sim_info.id)), 'sim': sim_info.full_name, 'chance': sickness_service.get_sickness_chance(SingleSimResolver(sim_info)), 'Sickness Chances': sickness_data, 'Examinations Performed': [{'interaction': str(interaction)} for interaction in exams_performed]})
    return sim_data

def archive_sim_sickness_event(sim_info, sickness, event_message):
    if sim_sickness_archiver.enabled:
        sim_sickness_archiver.archive(object_id=sim_info.id, data={'game_time': str(services.game_clock_service().now()), 'sickness': str(sim_info.current_sickness.__name__), 'event_type': event_message})
