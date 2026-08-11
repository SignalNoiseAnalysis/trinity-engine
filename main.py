from core import planner
from core import prompt_builder
from core import validator
from core import capability_registry
from capabilities import capability
from capabilities.lighting import lighting
import json

planner = planner.Planner('llama3.2:3b')
planner.load_validation_schema()
planner.load_planning_prompt()
prompt_builder = prompt_builder.PromptBuilder()

lighting = lighting.Lighting()
lighting.load_rules()
lighting.load_validation_schema()

registry = capability_registry.CapabilityRegistry()
registry.register(lighting)

print(registry.get_registry())

validator = validator.Validator()
# print(lighting.rules)
# print(planner.planning_prompt)
prompt = prompt_builder.build_prompt(lighting.rules, planner.planning_prompt)

commands = planner.plan(prompt)

for command in commands['commands']:
    print(validator.validate(command['command'], registry.get_registered_capability(command['capability']).get_validation_schema()))
    # lighting.handle_command(command["command"])
