from gsi_handlers.gameplay_archiver import GameplayArchiver
def log_outfit_change(sim_info, change_to, change_reason):
    if sim_info is None:
        return
    entry = {'change_from': repr(sim_info._current_outfit), 'change_to': repr(change_to), 'change_reason': repr(change_reason)}
    archiver.archive(data=entry, object_id=sim_info.id)
