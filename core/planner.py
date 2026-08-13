from ollama import chat
import json
import os

class Planner:

    def __init__(self, model):
        self.model = model
        self.load_envelope_validation_schema()
        self.load_intent_discovery_validation_schema()
        self.load_planning_prompt()
        self.load_intent_discovery_prompt()
        self.load_capability_command_wrapper_validation_schema()

    def plan(self, prompt):

        response = chat(
            model = self.model,
            messages = prompt
        )

        print(response['message']['content'])
        return json.loads(response['message']['content'])

    def load_envelope_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/validation/multiple_commands_envelope.json', 'r') as file:
            file_content = file.read()

        self.envelope_validation_schema = json.loads(file_content)

    def load_planning_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/prompts/planning.md', 'r') as file:
            file_content = file.read()

        self.planning_prompt = file_content

    def load_intent_discovery_prompt(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/prompts/capability_discovery.md', 'r') as file:
            file_content = file.read()

        self.intent_discovery_prompt = file_content

    def load_intent_discovery_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/validation/intent_discovery.json', 'r') as file:
            file_content = file.read()

        self.intent_discovery_validation_schema = json.loads(file_content)

    def load_capability_command_wrapper_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/planner/validation/capability_command_wrapper.json', 'r') as file:
            file_content = file.read()

        self.capability_command_wrapper_validation_schema = json.loads(file_content)