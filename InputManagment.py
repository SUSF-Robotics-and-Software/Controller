import json
import constructor


class InputDevice:
    def __init__(self):
        self.bindings = {}  # dict linking controls to inputs
        self.values = {}

    def set_binding(self, bind, command_name, command_parm):
        if type(self.bindings[bind]) == dict:
            self.bindings[bind][command_name] = command_parm
        else:
            self.bindings[bind] = {command_name: command_parm}

    def reset_binding(self, bind):
        self.bindings[bind] = {}

    def populate_bindings_from_JSON(self, profile_name):
        with open(profile_name + ".json", "r") as JSON_FILE:
            json_data = JSON_FILE.read()
            self.bindings = json.loads(json_data)

    def save_bindings(self, profile_name):
        with open(profile_name + ".json", "w") as JSON_FILE:
            JSON_FILE.write(json.dumps(self.bindings, indent=4, sort_keys=True))


class InputManager():
    def __init__(self):
        self.constructor = constructor.CommandCreator()
        self.constructor.create_class_source(command_primative)
        self.command_objs = {}
        self.input_devices = []
        self.command_state = None

    def output_commands(self):  # creates command objects from all inputs from all connected devices
        self.command_objs = {}
        for device in self.input_devices:
            for bind_name, bind_commands in device.bindings.items():
                for command_name, command_parm in bind_commands.items():
                    self.command_objs[command_name] = self.constructor.construct(command_name)
                    setattr(self.command_objs[command_name], command_parm, device.values[bind_name])
        return self.command_objs

    def create_output_string(self):  # creates a command set from all command objects
        self.command_state = command_set(self.command_objs) # from richard's commands
        return self.command_state.get_json()


"""
class controller(InputDevice):
    def get_values(self):
        events = get_gamepad()
        for event in events:
            if event.code != "SYN_REPORT":
                self.values[event.code] = event.value

class keyboard(InputDecive):
    def get_values(self):
        # HOWEVER YO GET KEYBOARD DATA
"""

