import brian.motors 
from brian.uicontrol import *
import brian.sensors 
import time
import math

ls = brian.sensors.EV3.ColorSensorEV3(brian.sensors.SensorPort.S1)
btn = brian.sensors.EV3.TouchSensorEV3(brian.sensors.SensorPort.S4)
Lmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.A)
Rmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.B)

class Global:
    black: float = 0
    white: float = 0
    gray: float = 0

def calibrate():
    print("calibrate white")
    btn.wait_for_press()
    Global.white = ls.reflected_value()
    time.sleep(0.5)
    print("calibrate black")
    btn.wait_for_press()
    Global.black = ls.reflected_value()
    Global.gray = (Global.black + Global.white)*0.5
    print(f"B:{Global.black} W:{Global.white} G:{Global.gray}")
#p = 1.5 d = 1.2 speed = 500
def pidReg():
    kp = 1.5
    ki = 0
    kd = 0.7
    error = (Global.gray- ls.reflected_value())/(Global.white - Global.black)
    last_error = error
    P = error
    I = 0
    D = error - last_error
    
    last_error = error
    return kp*P + ki*I +kd*D

def Main():
    ls.wait_until_ready()
    Lmtr.wait_until_ready()
    Rmtr.wait_until_ready()
    calibrate()
    while True:
        change = pidReg()
        basespeed = 800
        Lmtr.run_at_speed(int(basespeed*(1 - change)))
        Rmtr.run_at_speed(int(basespeed*(1 + change)))
        time.sleep(0.001)
Main()