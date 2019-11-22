#WIP
from tkinter import ttk
from tkinter import *
from InputManagmentV2 import *
from constructor import *

class GUI():
    def __init__(self):
        self.constructor = CommandCreator()
        self.constructor.create_class_source(command_primitive)

        self.root = Tk()
        self.root.geometry("500x500")
        self.input_manager = InputManager()
        self.tab_master = ttk.Notebook(self.root)
        self.tabs = {}
        self.dropdowns = {}

    def create_device(self, name, binding_profile):
        device = InputDevice(name)
        device.populate_bindings_from_JSON(binding_profile)
        self.input_manager.assign_device(device)

    def create_tab(self, tab_name):
        tab = ttk.Frame(self.tab_master)
        self.tabs[tab_name] = tab
        self.tab_master.add(self.tabs[tab_name], text=tab_name)
        self.tab_master.pack(expand=1, fill='both')

    def get_programmable_commands(self):

    def create_dropdown(self, master, name, values):
        variable = StringVar(master)
        variable.set(values[0])  # default value

        self.dropdowns[name] = OptionMenu(master, variable, *values)
        self.dropdowns[name].config(width = 20)
        self.dropdowns[name].pack()

    def dropdown_selection(self,master, name):




gui = GUI()
gui.create_device("controller1","profile1")
gui.create_device("controller2","profile3")
i=0
for device in gui.input_manager.input_devices:
    i+=1
    gui.create_tab(device.name)
    gui.create_dropdown(gui.tabs[("controller"+str(i))], ("commands dropdown_controller"+str(i)), list(device.get_inputs()))
print(gui.get_programmable_commands())
gui.root.mainloop()
