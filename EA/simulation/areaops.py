try:
    import _areaops
except ImportError:

    class _areaops:

        @staticmethod
        def op_request(*_, **__):
            pass

        @staticmethod
        def save_gsi(*_, **__):
            pass

        @staticmethod
        def load_gsi(*_, **__):
            pass

        @staticmethod
        def trigger_assert(*_, **__):
            pass
