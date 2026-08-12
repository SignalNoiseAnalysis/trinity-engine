from core import planner
from core import prompt_builder
from core import validator
from core import capability_registry
from core import executor
from capabilities import capability
from capabilities.lighting import lighting
import json

planner = planner.Planner('llama3.2:3b')

prompt_builder = prompt_builder.PromptBuilder()

lighting = lighting.Lighting()

registry = capability_registry.CapabilityRegistry()
registry.register(lighting)

executor = executor.Executor()

validator = validator.Validator()
prompt = prompt_builder.build_prompt(lighting.description, planner.capability_discovery_prompt)

commands = planner.plan(prompt)

print(commands)

# for command in commands['commands']:
#     if validator.validate(command['command'], registry.get_registered_capability(command['capability']).get_validation_schema()):
#         executor.execute_command(registry.get_registered_capability(command['capability']), command["command"])
