import brian.motors as motors
import brian.sensors as sensors
import time

rm = motors.NXTMotor(motors.MotorPort.A)
lm = motors.NXTMotor(motors.MotorPort.B)
ls =sensors.NXT.LightSensorNXT(sensors.SensorPort.S1)
speed = 100


while True:
    print("CW[A]...")
    rm.wait_until_ready()
    lm.wait_until_ready()
    rm.run_at_speed(speed)
    lm.run_at_speed(speed)

    print("Wait...")
    time.sleep(1)
