import os
from capabilities import capability

class Executor():
    
    def __init__(self):
        pass

    def execute_command(self, capability, command):
        capability.handle_command(command)
