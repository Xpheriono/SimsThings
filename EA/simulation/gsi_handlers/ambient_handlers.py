from gsi_handlers.gameplay_archiver import GameplayArchiver
def archive_ambient_data(description, created_situation=''):
    entry = {}
    entry['sources'] = description
    entry['created_situation'] = created_situation
    archiver.archive(data=entry)
