from capabilities import capability

class CapabilityRegistry():

    def __init__(self):
        self.registry = {}

    def register(self, capability):
        self.registry[capability.get_name()] = capability

    def get_registry(self):
        return self.registry

    def get_registered_capability(self, capability):
        return self.registry[capability]