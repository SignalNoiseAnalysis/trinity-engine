from abc import ABC, abstractmethod
import json

class Capability(ABC):

    def __init__(self):
        self.x = 5

    @abstractmethod
    def load_description(self):
        pass

    @abstractmethod
    def load_actions(self):
        pass

    @abstractmethod
    def load_rules(self):
        pass

    @abstractmethod
    def handle_command(self, command):
        pass

