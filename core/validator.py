import json
import os
from jsonschema import validate, ValidationError

class Validator():

    def validate(self, instance, schema):
        try:
            validate(instance=instance, schema=schema)
            return True
        except:
            return False