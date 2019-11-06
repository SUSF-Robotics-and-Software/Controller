class InputDevice:
    def __init__(self):
        self.bindings = {}  # dict linking controls to inputs
        self.values = {}

    def set_binding(self, bind, command_name, command_parm):
        if type(self.bindings[bind]) == dict:
            self.bindings[bind][command_name] = command_parm
        else:
            self.bindings[bind] = {command_name:command_parm}

    def reset_binding(self,bind):
        self.bindings[bind] = {}

    def populate_bindings_from_JSON(self,profile_name):
        with open(profile_name+".json","r") as JSON_FILE:
            json_data = JSON_FILE.read()
            self.bindings = json.loads(json_data)

    def save_bindings(self,profile_name):
        with open(profile_name+".json","w") as JSON_FILE:
            JSON_FILE.write(json.dumps(self.bindings, indent=4, sort_keys=True))

    #def get_values(self):