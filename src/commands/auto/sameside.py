import wpilib
from wpilib.command import CommandGroup
from commands.drivetodistance import DriveToDistance
from commands.turndrive import TurnDrive
from commands.auto.donothing import DoNothing
from commands.autoarmextender import AutoArmExtender
# TODO: Add import statement for the DriveToCube and DeliverCube Command.
#from commands.runintake import RunIntake

from commands.tankdrivetimed import TankDriveTimed
from commands.grabber import Grabber

from robotmap import measures, auto_measures, inches, waits
import math

"""
Route Approximation:
          Scale
          \   /
           \ /
            |\ 
            | \ 
            |  \ 
            |   Cube
            |
        Startpoint
"""


class SameSide(CommandGroup):
    def __init__(self, direction):
        super().__init__("SameSide")
        self.direction = direction
        # import it here
        from commands.auto import Direction
        print ("__init__ sameside")
        #if _direction:
            # Left
        #    direction = 1
        #else:
            # Right
        #    direction = -1
        
        if direction == Direction.MIDDLE:
            print ("warning, passed Direction.MIDDLE to a side command, doing nothing")
            return

        # Drive Forward 10 ft

        end_point = auto_measures.to_scale - inches(30)
        start_turning_point = end_point - inches(46)

        #Raise Arm if not raised
        self.addSequential(AutoArmExtender(True))

        self.addSequential(DriveToDistance(
            start_turning_point, 
            start_turning_point
        ), 4.5)
        

        # drive then turn absed on direction
        print ("DIRECTION: " + str(direction))

        # Turn Slightly towards goal. NOTE: Look into raising arm before you get to the scale.
        if direction == Direction.LEFT:
            print('running same side left')
            self.addSequential(DoNothing(waits.turn))

            # turn towards the scale and then drive towards it
            self.addSequential(TurnDrive(-auto_measures.angle_switch), 2.0)
            #dist = end_point - start_turning_point, auto_measures.robot_starting_offset)
            #dist = math.hypot(end_point - start_turning_point, auto_measures.robot_starting_offset)
            self.addSequential(AutoArmExtender(True))
            self.addSequential(DoNothing(3))
            #self.addSequential(RunIntake(1.0), 1.0)
      
        elif direction == Direction.RIGHT:
            print('running same side right')
            self.addSequential(DoNothing(waits.turn))

            # turn towards the scale and then drive towards it
            self.addSequential(TurnDrive(auto_measures.angle_switch), 2.0)
            #dist = end_point - start_turning_point, auto_measures.robot_starting_offset)
            #dist = math.hypot(end_point - start_turning_point, auto_measures.robot_starting_offset)
            self.addSequential(AutoArmExtender(True))
            self.addSequential(DoNothing(3))
            #self.addSequential(RunIntake(1.0), 1.0)

        # self.addSequential(LiftToProportion(measures.ROBOT_ARM_SCALE_DROP), 5.0)

        #self.addSequential(DoNothing(1.2))

       # self.addSequential(AutoArmExtender(True))
        
       # self.addParallel(TankDriveTimed(.34, .34, .4))

       # self.addSequential(DoNothing(1.2))

       # self.addSequential(RunIntake(1.0), 1.0)
            

        # Raise Arm and extend (Deliver Cube Method)
        # self.addSequential( [Imported Cube Delivery method] )

        # Turn to cube TODO: Find this 
        #if direction == Direction.LEFT:
        
        
        #self.addSequential(DoNothing(5))

        #self.addSequential(TurnDrive(90*direction))

        # Move to Cube
        # self.addSequential( [Imported Cube Location function here] )
        # self.addSequential( [Imported Cube Delivery method] )
