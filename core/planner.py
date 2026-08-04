from ollama import chat
import json

class Planner:

    def __init__(self, model, system_prompt):
        self.model = model
        self.system_prompt = system_prompt

    def plan(self):
        prompt = build_prompt()

        response = chat(
            model = self.model,
            messages = build_prompt()
        )

        print(response['message']['content'])

def build_prompt():
    return [
        {
            "role":"system",
            "content": 'You are the planner for an AI Agent',
        },
        {
            "role":"user",
            "content": 'Turn on all of the lights'
        }
    ]
