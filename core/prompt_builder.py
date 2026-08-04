import json
import os

class PromptBuilder:

    def __init__(self):
        self.x = 5
        self.planning = ''

    def build_prompt(self, capability):
        return [
            {
                "role":"system",
                "content": self.planning + "\n" + capability,
            },
            {
                "role":"user",
                "content": 'Turn on all of the lights'
            }
        ]

    def get_planning_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/prompts/planning.md', 'r') as file:
            file_content = file.read()

        self.planning = file_content