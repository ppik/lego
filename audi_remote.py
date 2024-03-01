from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

remote = Remote()

motor_front = Motor(Port.A, Direction.CLOCKWISE)
motor_rear = Motor(Port.B, Direction.CLOCKWISE)
motor_steer = Motor(Port.D, Direction.CLOCKWISE)

car = Car(motor_steer, [motor_front, motor_rear])

while True:
    pressed = remote.buttons.pressed()

    steering = 0
    if Button.LEFT_PLUS in pressed:
        steering += 100
    if Button.LEFT_MINUS in pressed:
        steering -= 100
    car.steer(steering)

    power = 0
    if Button.RIGHT_PLUS in pressed:
        power += 100
    if Button.RIGHT_MINUS in pressed:
        power -= 100
    car.drive_power(power)

    wait(10)