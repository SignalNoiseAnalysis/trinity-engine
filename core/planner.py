from ollama import chat
import json

class Planner:

    def __init__(self, model):
        self.model = model

    def plan(self, prompt):

        response = chat(
            model = self.model,
            messages = prompt
        )

        print(response['message']['content'])
