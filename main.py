from core import planner
from core import prompt_builder
from capabilities import capability
from capabilities.lighting import lighting
import json

planner = planner.Planner('llama3.2:3b')
prompt_builder = prompt_builder.PromptBuilder()
prompt_builder.get_planning_prompt()

lighting = lighting.Lighting()
lighting.load_rules()

prompt = prompt_builder.build_prompt(lighting.rules)
commands = planner.plan(prompt)

for command in commands['commands']:
    lighting.handle_command(command)
