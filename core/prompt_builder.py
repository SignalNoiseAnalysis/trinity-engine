import json
import os

class PromptBuilder:

    def __init__(self):
        self.x = 5

    def build_prompt(self, capability, planner):
        return [
            {
                "role":"system",
                "content": planner + "\n" + capability,
            },
            {
                "role":"user",
                "content": 'Turn off all of the lights and check the weather'
            }
        ]