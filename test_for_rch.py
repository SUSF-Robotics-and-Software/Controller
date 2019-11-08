from abstract_class_definitions import *

class single_value_data(command_primitive):
    def __init__(self, name):
        self.name = name
        self.value = None

class sample1(command_primitive):
    def __init__(self, name):
        self.name = name
        self.velocity = 0
        self.curvature = 0


command_name = "sample1"
command_parm = []
command_parm.append(single_value_data("velocity"))
command_parm[-1].value = 1
command_parm.append(single_value_data("curvature"))
command_parm[-1].value = 1


cmdSet = command_set(*command_parm, name=command_name)
print(cmdSet)
print(cmdSet.get_json())