#!/usr/bin/python3
"""contains the "to_json_string" function"""
import json


def to_json_string(my_obj):
    """Returns the Json representation of an object (string)"""
    return json.dumps(my_obj)
