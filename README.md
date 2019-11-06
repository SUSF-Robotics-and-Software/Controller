# Input-Manager
Human input to command state

## problem definition

To do the _rover_ input manager, we could just define all the commands we need
in the file. For a generic input controller, we want an external source for

1.  the available commands
2.  the mapping of the controls to those commands

The **actionable parameters** (e.g. curvature, forward_velocity) are defined
by the locomotion controller. These therefore need to be pulled from the
locomotion controller module. 

The **controller inputs** (e.g.  WASD keypress, analogue stick X axis value)
are defined by the controller. If we abstract these to, or just pre-define,
a fixed set, then they can be sourced from here. The **high level commands**
are then "move forward, turn left". They are mapped by the locomotion
controller to the actionable parameters. The controller inputs are mapped
to the high level commands by this module.
