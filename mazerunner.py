#r = 3,8cm
#rozvor = 15,5cm
import brian.motors 
from brian.uicontrol import *
import brian.sensors 
import time
import math

ls = brian.sensors.EV3.ColorSensorEV3(brian.sensors.SensorPort.S1)
btn = brian.sensors.EV3.TouchSensorEV3(brian.sensors.SensorPort.S4)
Lmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.A)
Rmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.B)

def ninety_deg_turn():
    Rmtr.rotate_by_angle(233,200)
    Lmtr.rotate_by_angle(233,200)

def Main():
    ls.wait_until_ready()
    Lmtr.wait_until_ready()
    Rmtr.wait_until_ready()
    
Main()