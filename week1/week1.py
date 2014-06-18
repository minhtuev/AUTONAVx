import quadrotor.command as cmd
from math import sqrt

def plan_mission(mission):

    # this is an example illustrating the different motion commands,
    # replace them with your own commands and activate all beacons
    commands  = [
        cmd.forward(1),
        cmd.up(1),
        cmd.left(2),
        cmd.forward(4),
        cmd.right(2),
        cmd.backward(4),
        cmd.right(2),
        cmd.forward(4),
    ]

    mission.add_commands(commands)
