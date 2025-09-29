import brian.motors 
import brian.sensors 
import time
import math

ls = brian.sensors.EV3.ColorSensorEV3(brian.sensors.SensorPort.S1)
btn = brian.sensors.EV3.TouchSensorEV3(brian.sensors.SensorPort.S4)
Lmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.A)
Rmtr = brian.motors.EV3LargeMotor(brian.motors.MotorPort.D)

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


def pidReg():
    kp = 1
    ki = 0
    kd = 0
    error = (Global.gray - ls.reflected_value())/(Global.white - Global.gray)
    P = error
    I = 0
    D = 0
    
    last_error = error
    return kp*P + ki*I +kd*D

def Main():
    while True:
        change = pidReg()
        basespeed = 100
        Lmtr.run_at_speed(int(basespeed*(1 + change)))
        Rmtr.run_at_speed(int(basespeed*(1 - change)))
        time.sleep(10)
Main()