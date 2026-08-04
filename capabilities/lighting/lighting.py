import json
import sys
import os

sys.path.append('../capabilities')

from capabilities import capability

class Lighting(capability.Capability):

    def provide_description(self):
        self.y = 5

    def provide_actions(self):
        self.x = 5

    def load_rules(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/rules.md', 'r') as file:
            file_content = file.read()

        self.rules = file_content
