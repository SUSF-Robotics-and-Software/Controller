from abstract_class_definitions import *
from generic_command_classes import *

class set_type(): pass


class command_data():
    def __init__(self, name, cmd_type, data_type, data):
        self.name = name
        self.data_type = data_type
        self.cmd_type = cmd_type
        self.data = data


def all_subclasses(cls):
    class_list = []
    for clss in cls.__subclasses__():
        class_list.append(clss)
        clss_subclasses = all_subclasses(clss)
        if len(clss_subclasses) > 0:
            class_list += clss_subclasses
    return class_list

def create_command(cmd_data):
    cmd_set = {}
    cmd_source = all_subclasses(command_primitive)
    for cmd in cmd_source:
        cmd_set[cmd.__name__] = cmd

    cmd_set[cmd_data.cmd_type] = type(cmd_data.cmd_type, (set_type,), {})

    resultant_command = type(cmd_data.name, (cmd_set[cmd_data.cmd_type],cmd_set[cmd_data.data_type]), {})
    cmd = resultant_command(cmd_data.name, cmd_data.data)
    return cmd
