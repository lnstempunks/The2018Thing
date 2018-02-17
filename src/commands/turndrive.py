import wpilib

from wpilib.command import Command
from wpilib.pidcontroller import PIDController
import subsystems
from robotmap import pid, Gearing
from pid.pidnavx import PIDNavXSource


class TurnDrive(Command):
    def __init__(self, _angle):
        super().__init__('TurnDrive')

        self.angle = _angle

        def set_opposite(pw):
            wpilib.SmartDashboard.putNumber("TurnDrive pidOutput", pw)
            subsystems.tankdrive.set_right(pw)
            subsystems.tankdrive.set_left(-pw)

        #self.navx = PIDNavXSource(subsystems.sensors.navx)
        self.PID = PIDController(pid.angle[0], pid.angle[1], pid.angle[2], pid.angle[3], subsystems.sensors.navx.getYaw, set_opposite)

        self.PID.setInputRange(-180.0, 180.0)
        self.PID.setOutputRange(-1.0, 1.0)
        self.PID.setContinuous(True)
        self.PID.setAbsoluteTolerance(0.35)

    def initialize(self):
        self.val = subsystems.sensors.navx.getYaw() + self.angle
        while self.val > 180:
            self.val -= 360.0
        while self.val < -180:
            self.val += 360
        self.PID.enable()

    def execute(self):
        wpilib.SmartDashboard.putData("Angle PID", self.PID)
        wpilib.SmartDashboard.putNumber("Angle PID Setpoint", self.val)
        subsystems.dump_info()
        self.PID.setSetpoint(self.val)
        

    def end(self):
        self.PID.disable()
        subsystems.tankdrive.stop()


    def isFinished(self):
        return self.PID.onTarget()
        #return False

