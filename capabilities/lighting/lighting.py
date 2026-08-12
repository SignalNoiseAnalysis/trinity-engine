import json
import sys
import os
from dotenv import load_dotenv
from govee import GoveeClient, Colors

sys.path.append('../capabilities')

from capabilities import capability

class Lighting(capability.Capability):

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GOVEE_API_KEY")
        self.client = GoveeClient(api_key=self.api_key, prefer_lan=True)
        self.devices = self.client.discover_devices()
        self.name = "Lighting"

        self.load_validation_schema()
        self.load_description()
        self.load_actions()
        self.load_rules()


    def get_name(self):
        return self.name

    def get_validation_schema(self):
        return self.validation_schema

    def load_description(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/description.md', 'r') as file:
            file_content = file.read()
        
        self.description = file_content

    def load_actions(self):
        self.x = 5

    def load_rules(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/rules.md', 'r') as file:
            file_content = file.read()

        self.rules = file_content

    def load_validation_schema(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/command_schema.json', 'r') as file:
            file_content = file.read()

        self.validation_schema = json.loads(file_content)

    def handle_command(self, command):
        if command['intent'] == 'control_lights':
            if command['action'] == 'set_state':
                if command['target']['type'] == 'room':
                    rooms = {}
                    for room in self.client.discover_devices():
                        if room.sku == "BaseGroup":
                            rooms[room.name] = room
                    room = rooms[command['target']['id']]
                    if command['parameters']['power'] == 'off':
                        self.client.power(room, on=False)
                    elif command['parameters']['power']== 'on':
                        self.client.power(room, on=True)
