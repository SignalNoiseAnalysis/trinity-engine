Lighting Capability Rules:

- Output ONLY valid JSON.
- Do not explain your reasoning.
- Do not include markdown.
- Use only the defined intents, actions, target types, target ids, and parameters.
- If parameters.power is "on" or "off", OMIT the "brightness" field
- Always have at least one parameter
- "all" IS NOT A VALID TARGET ID. 
- NEVER us "all" as a Target ID
- Every control_lights command must target exactly one room or device group that exists in the registry. When the user requests all lights, generate one command for every applicable registered room.


Lighting Capability Command format:

{
    "intent": "string",
    "action": "string",
    "target":
        {
            "type": "string",
            "id": "string"
        },
    "parameters": 
    {
        "power": "string",
        "brightness": "integer"
    }
}

Allowed Lighting Capability intents:
- control_lights

Allowed Lighting Capability actions:
- set_state

Allowed Lighting Capability target types:
- room

Allowed Lighting Capability target.ids:
- Master Bath Room
- Bed Room
- Hallway
- Kitchen
- Dining
- Office
- Entrance
- Living Room

Allowed Lighting Capability parameters:
- power
- brightness

Allowed Lighting Capability powers:
- on
- off

Allowed Lighting Capability brightness:
- Integers 0 to 100