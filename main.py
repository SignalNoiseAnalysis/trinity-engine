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
executor = executor.Executor()
validator = validator.Validator()
registry = capability_registry.CapabilityRegistry()

lighting = lighting.Lighting()

registry.register(lighting)

capability_descriptions = ""
for key in registry.registry.keys():
    capability_descriptions += registry.registry[key].description
    capability_descriptions += "\n"

capability_discovery_prompt = prompt_builder.build_prompt(capability_descriptions, planner.intent_discovery_prompt)

discovered_capabilities = planner.plan(capability_discovery_prompt)

if validator.validate(discovered_capabilities, planner.intent_discovery_validation_schema):

    capability_rules = ""
    for capability in discovered_capabilities["capabilities"]:
        capability_rules += registry.registry[capability.lower()].rules
        capability_rules += "\n"

    command_prompt = prompt_builder.build_prompt(capability_rules, planner.planning_prompt)

    commands = planner.plan(command_prompt)

    if validator.validate(commands, planner.envelope_validation_schema):
        print("Woo!")
        for command in commands["commands"]:
            print(command)
            if validator.validate(command, planner.capability_command_wrapper_validation_schema):
                print("Woohoo!")
                if validator.validate(command['command'], registry.get_registered_capability(command['capability'].lower()).get_validation_schema()):
                    print("YEEEEHAWWWW!")
                    executor.execute_command(registry.get_registered_capability(command['capability'].lower()), command["command"])
