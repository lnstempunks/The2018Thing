import wpilib

from wpilib.command.subsystem import Subsystem
from wpilib import PIDController
from wpilib.pidcontroller import PIDController

from hardware.motor import Motor
from hardware.solenoid import SolenoidHandler
from hardware.encoder import Encoder

from commands.tankdrivejoystick import TankDriveJoystick

from robotmap import drive_motors, drive_encoders, solenoids
from robotmap import Gearing

from puremath.scaling import transform

from enum import Enum


class TankDrive(Subsystem):
    """

    This example subsystem controls a single CAN Talon SRX in PercentVBus mode.
    
    Edit on 1-20-2018: Future Encoder code is commented out. Added Solenoid objects for gearshifting
    
    """

    def __init__(self):

        super().__init__("TankDrive")

        self.motors = {
            "LF": Motor(*drive_motors.LF),
            "LB": Motor(*drive_motors.LB),
            "RF": Motor(*drive_motors.RF),
            "RB": Motor(*drive_motors.RB)
        }

        self.encoders = {
            "L": Encoder(*drive_encoders.L),
            "R": Encoder(*drive_encoders.R)
        }

        self.encoders["L"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        self.encoders["R"].setPIDSourceType(PIDController.PIDSourceType.kRate)
        
        # Now they are the same kind of encoder.        
        self.encoders["L"].setDistancePerPulse(drive_encoders.L_dpp)
        self.encoders["R"].setDistancePerPulse(drive_encoders.R_dpp)

        self.gearshift = SolenoidHandler(*solenoids.gearshift)


    def set_left(self, power):
        self.motors["LF"].set(power)
        self.motors["LB"].set(power)
    
    def set_right(self, power):
        self.motors["RF"].set(power)
        self.motors["RB"].set(power)

    def get_left_distance(self):
        return self.encoders["L"].getDistance()

    def get_right_distance(self):
        return self.encoders["R"].getDistance()

    def stop(self):
        self.set(0, 0)

    def set(self, Lpower=0, Rpower=0):
        if Lpower is not None:
            self.set_left(Lpower)

        if Rpower is not None:
            self.set_right(Rpower)

    def get_gearing(self):
        get = self.gearshift.get()
        if get == False:
            return Gearing.LOW
        elif get == True:
            return Gearing.HIGH
        else:
            raise Exception("internal problem calculating gearing")

    def set_gearing(self, gear):
        if gear == Gearing.LOW:
            self.gearshift.set(False)

        elif gear == Gearing.HIGH:
            self.gearshift.set(True)

        else:
            raise Exception("setting gearing to unknown gear")

