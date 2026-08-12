from ollama import chat
import json
import os

class Planner:

    def __init__(self, model):
        self.model = model
        self.load_validation_schema()
        self.load_planning_prompt()
        self.load_capability_discovery_prompt()

    def plan(self, prompt):

        response = chat(
            model = self.model,
            messages = prompt
        )

        print(response['message']['content'])
        return json.loads(response['message']['content'])

    def load_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/validation/planning.json', 'r') as file:
            file_content = file.read()

        self.validation_schema = json.loads(file_content)

    def load_planning_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/prompts/planning.md', 'r') as file:
            file_content = file.read()

        self.planning_prompt = file_content

    def load_capability_discovery_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/prompts/capability_discovery.md', 'r') as file:
            file_content = file.read()

        self.capability_discovery_prompt = file_content