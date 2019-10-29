from gsi_handlers.gameplay_archiver import GameplayArchiver
    sub_schema.add_field('team_name', label='Name', width=1)
    sub_schema.add_field('team_members', label='Members', width=1)
    sub_schema.add_field('team_score', label='Score', width=1)
    sub_schema.add_field('team_rounds_taken', label='Rounds Taken', width=1)
@GsiHandler('game_info', game_component_schema)
def generate_game_info_data():
    game_info = []
    for obj in services.object_manager().get_all_objects_with_component_gen(objects.components.types.GAME_COMPONENT):
        if obj.game_component.current_game is None:
            pass
        else:
            game = obj.game_component
            if game.winning_team is not None:
                winning_sims = ','.join([str(sim) for sim in game.winning_team.players])
            else:
                winning_sims = 'None'
            if game.high_score_sim_ids is not None:
                high_score_sim_ids = str(game.high_score_sim_ids)
            else:
                high_score_sim_ids = 'None'
            entry = {'current_game': str(game.current_game), 'target_object': str(game.target_object), 'number_of_players': str(game.number_of_players), 'winning_sims': winning_sims, 'joinable': str(game.is_joinable()), 'requires_setup': str(game.requires_setup), 'game_over': str(game.game_has_ended), 'high_score': game.high_score, 'high_score_sim_ids': high_score_sim_ids}
            entry['teams'] = [{'team_name': game.get_team_name(i), 'team_members': ';'.join(str(sim) for sim in team.players), 'team_score': team.score, 'team_rounds_taken': team.rounds_taken} for (i, team) in enumerate(game._teams)]
            game_info.append(entry)
    return game_info

def archive_game_log_entry(game_object, log_entry_str):
    entry = {'game_object': str(game_object), 'log': log_entry_str}
    game_log_archiver.archive(data=entry)
