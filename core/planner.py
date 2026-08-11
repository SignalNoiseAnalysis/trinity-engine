from ollama import chat
import json
import os

class Planner:

    def __init__(self, model):
        self.model = model

    def plan(self, prompt):

        response = chat(
            model = self.model,
            messages = prompt
        )

        print(response['message']['content'])
        return json.loads(response['message']['content'])

    def load_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/validator/planning.json', 'r') as file:
            file_content = file.read()

        self.validation_schema = json.loads(file_content)

    def load_planning_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/prompts/planning.md', 'r') as file:
            file_content = file.read()

        self.planning_prompt = file_content