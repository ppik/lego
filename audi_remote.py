from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

motor_front = Motor(Port.A, Direction.CLOCKWISE)
motor_rear = Motor(Port.B, Direction.CLOCKWISE)
motor_steer = Motor(Port.D, Direction.CLOCKWISE)

car = Car(motor_steer, [motor_front, motor_rear])
remote = Remote()

while True:
    pressed = remote.buttons.pressed()

    steering = 0
    if Button.LEFT_PLUS is pressed:
        steering += 100
    if Button.LEFT_MINUS is pressed:
        steering -= 100
    car.steer(steering)

    power = 0
    if Button.RIGHT_PLUS is pressed:
        power += 100
    if Button.RIGHT_MINUS is pressed:
        power -= 100
    car.drive_power(power)

    wait(10)