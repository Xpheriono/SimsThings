from sims4.service_manager import Service
class ContentModes(DynamicEnum):
    PRODUCTION = 0
    DEMO = 1

class ConfigService(Service):
    DEFAULT_CONTENT_MODE = TunableEnumEntry(ContentModes, default=ContentModes.PRODUCTION, description='Content mode that the server starts up in.')

    def __init__(self):
        self.content_mode = self.DEFAULT_CONTENT_MODE
