"""

interface for the wires

"""

class InfoPasser:
    """
    
    Dummy class used to store variables on an object.
    
    """
    pass


drive_motors = InfoPasser()

# L = left, R = right, F = front, B = back
# each object has (port, reverse)
drive_motors.LF = 0, False
drive_motors.LB = 1, False
drive_motors.RF = 2, False
drive_motors.RB = 3, False

#L = left, R = right, E = Encoder
# Each encoder has two ports on the RoboRIO DIO 
encoders = InfoPasser()
encoders.L_E = 2, 3
encoders.R_E = 0, 1

axes = InfoPasser()

axes.L_x = 0
axes.L_y = 1

axes.R_x = 2
axes.R_y = 5


