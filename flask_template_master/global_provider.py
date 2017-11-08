class BaseGlobalProvider:
    def get_globals(self):
        """Get a dictionary of global values."""
        raise NotImplementedError()


class DictGlobalProvider(BaseGlobalProvider):
    GLOBALS = None

    def __init__(self, global_variables):
        self.GLOBALS = global_variables

    def get_globals(self):
        return self.GLOBALS
