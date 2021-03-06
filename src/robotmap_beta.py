"""

interface for the wires

Edit 1-20-2018: Encoder class created

"""
from robotmap import InfoPasser, NavXType


drive_motors = InfoPasser()

# L = left, R = right, F = front, B = back
# each object has (port, reverse)
drive_motors.LF = 0, True
drive_motors.LB = 1, True
drive_motors.RF = 2, False
drive_motors.RB = 3, False


arm_stopper = InfoPasser()
arm_stopper.dio = 6
arm_stopper.default = True




drive_encoders = InfoPasser()

# Each encoder has two ports on the RoboRIO DIO
# Then, "inverted"
drive_encoders.L = 0, 1, False
drive_encoders.R = 2, 3, True

# distance per pulse
drive_encoders.L_dpp = 1.0/(.875 * 1.524 * 1610.0)
drive_encoders.R_dpp = 1.0/(.875 * 1.524 * 1610.0)

# range is a min, max of what speed (in ticks/time) are the encoders reading
# lowgear is for low gear readings and highgear is for high gear readings
# Left Encoder - 2454 Ticks in ~5 Feet
# Right Encoder - 2414 Ticks in ~5 Feet
# L.H = left high gear
# L.L = left low gear

drive_encoders.L_H = (-4.85 * .98, 4.85 * .98)
drive_encoders.R_H = (-4.85, 4.85)
drive_encoders.L_L = (-2.24 * .98, 2.24 * .98)
drive_encoders.R_L = (-2.24, 2.24)


# was extra_motors
arm_motors = InfoPasser()
arm_motors.L = 4, False
arm_motors.R = 5, False

arm_encoders = InfoPasser()

# Each encoder has two ports on the RoboRIO DIO
# Then, "inverted"
arm_encoders.L = 4, 5, True
arm_encoders.R = 6, 7, False

# the scale so that it is from (0, 1)
arm_encoders.L_dpp = 1.0/950.0
arm_encoders.R_dpp = 1.0/950.0




joystick_info = InfoPasser()

joystick_info.error = 0.05


# PID controller


axes = InfoPasser()

axes.L_x = 0
axes.L_y = 1

axes.R_x = 2
axes.R_y = 5


# triggers
axes.L_t = 3
axes.R_t = 4



solenoids = InfoPasser()

# solenoid ports
# main and complimentary ports and inverted
# port 0, port 1, isInverted
solenoids.gearshift = [(0, False), (1, True)]
solenoids.grabber = [(4, True), (5, False)]


# arm extender
solenoids.armextender = [(2, True), (3, False)]

solenoids.final_armextender = [(6, False), (7, True)]

#solenoids.gearshift1 


# RoboRIO Analog In Port for the analog pressure sensor
solenoids.pressure_sensor = 0

# The supply voltage for the analog pressure sensor
solenoids.supply_voltage = 5




navx_type = NavXType.SPI

# PID Constant values for the encoders. CHECK OVER!!!!!
pid = InfoPasser()
pid.L = (0.15, 0, 0, 0)
pid.R = (0.15, 0, 0, 0)
pid.dist_L = (1.7, 0, 0, 0)
pid.dist_R = (1.7, 0, 0, 0)

pid.angle = (0.014, 0, 0, 0)



measures = InfoPasser()
# in meters
measures.ROBOT_WHEELTOWHEEL_WIDTH = 0.64

# the radius (in meters), cutoff that the MoveToBox command stops moving at
measures.ROBOT_CUBE_DISTANCE_CUTOFF = 0.67

# the angle range the arm can operate in
#measures.ROBOT_ARM_ANGLE_RANGE = (-45.0, 90.0)

measures.ROBOT_ARM_RANGE = (0.0, 1.0)

# TODO: measures these as proportions
measures.ROBOT_ARM_RETRACT_RANGE = (.0834, .8484)

measures.ROBOT_ARM_HORIZONTAL = 0.41

measures.ROBOT_ARM_SWITCH_DROP = 0.41
measures.ROBOT_ARM_SCALE_DROP = 0.92


measures.ROBOT_ARM_RETRACT_TIME = 2.8







