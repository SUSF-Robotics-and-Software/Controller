from abstract_commands import *
from generic_command_classes import *
import inputs
import os
import threading


class InputDevice:
    def __init__(self, name):
        self.name = name
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
        os.chdir(".\\InputManager")
        with open(profile_name + ".json", "r") as JSON_FILE:
            json_data = JSON_FILE.read()
            json_data = json.loads(json_data)
            self.bindings = json_data[0]
            self.control_proporties = json_data[1]
            self.init_values()

    def save_bindings(self, profile_name):
        with open(profile_name + ".json", "w") as JSON_FILE:
            JSON_FILE.write(json.dumps(self.bindings, indent=4, sort_keys=True))

    def get_inputs(self):
        return self.bindings.keys()

    def init_values(self):
        for key in self.control_proporties:
            self.values[key] = 0;


class Controller(InputDevice):
    def __init__(self, name):
        super().__init__(name)


    def get_values(self):
        # self.values = DEVICE INPUT
        while(True):
            events = inputs.get_gamepad()
            for event in events:
                if event.code != "SYN_REPORT":
                    self.values[event.code] = event.state
                    self.normalise(event.code)
                    self.check_tolerances(event.code)

    def check_tolerances(self,input):
        if abs(self.values[input]) < self.control_proporties[input][1]:
            self.values[input] = 0

    def normalise(self,input):
        self.values[input] = self.values[input] / self.control_proporties[input][0]

class InputManager():
    def __init__(self):
        self.command_objs = {}
        self.input_devices = []
        self.command_state = None
        with open("abstract_commands_list.json", "r") as FILE:
            self.cmd_types = json.loads(FILE.read())

    def assign_device(self, device):
        self.input_devices.append(device)

    def update_devices(self):
        self.device_threads = []
        for device in self.input_devices:
            self.device_threads.append(threading.Thread(target=device.get_values))
            self.device_threads[-1].start()

    def output_commands(self):  # creates command objects from all inputs from all connected devices
        self.command_objs = []
        for device in self.input_devices:
            for bind_name, bind_command in device.bindings.items():
                cmd_data = command_data(bind_command, self.cmd_types[bind_command][0], self.cmd_types[bind_command][1],
                                        self.cmd_types[bind_command][2:])  # construct command data
                self.command_objs.append(create_command(cmd_data))
                self.command_objs[-1].value = device.values[bind_name]
        return self.command_objs

    def output_command_sets(self):
        command_set_dict = {}
        for typ in set_type.__subclasses__():
            command_set_dict[typ.__name__] = []

        for command in self.command_objs:
            for typ in set_type.__subclasses__():
                if isinstance(command, typ):
                    command_set_dict[typ.__name__].append(command)

        command_sets = []
        for key in command_set_dict:
            values = command_set_dict[key]
            command_sets.append(command_set(name=key, *values))

        return command_sets

    def output_loop(self):
        update_time = 1.0
        output_thread = threading.Timer(update_time, self.output_loop)
        output_thread.start()
        self.output_commands()
        print(self.output_command_sets())



device = Controller("device1")
device.populate_bindings_from_JSON("xbox_controller")
inpMan = InputManager()
inpMan.assign_device(device)


inpMan.update_devices()

inpMan.output_loop()


