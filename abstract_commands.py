from abstract_class_definitions import *


class single_value_data(command_primitive):
    def __init__(self, name):
        self.name = name
        self.value = None


class multiple_value_data(command_primitive):
    def __init__(self, name):
        self.name = name
        self.value = []


class set_type(): pass


class command_data():
    def __init__(self, name, types):
        self.name = name
        self.types = types


class command():
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


def create_command(cmd_data):
    cmd_set = {}
    cmd_source = command_primitive.__subclasses__()  # + set_type.__subclasses__()
    for cmd in cmd_source:
        cmd_set[cmd.__name__] = cmd

    for type_name in cmd_data.types:
        if type_name not in cmd_set:
            cmd_set[type_name] = type(type_name, (set_type,), {})

    types = []
    for type_name in cmd_data.types:
        types.append(cmd_set[type_name])

    resultant_command = type(cmd_data.name, (command, *types), {})

    return resultant_command(cmd_data.name)  # command(command_data.name)
