from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import Light, Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait, StopWatch

hub = TechnicHub()
remote = Remote()

motor_front = Motor(Port.A, Direction.CLOCKWISE)
motor_rear = Motor(Port.B, Direction.CLOCKWISE)
motor_steer = Motor(Port.D, Direction.CLOCKWISE)

car = Car(motor_steer, [motor_front, motor_rear])

light = Light(Port.C)
watch = StopWatch()

light_cycle = [0, 10, 60, 100]
light_level = 0
light_pressed = 0

hub.light.on(Color.GREEN)
remote.light.on(Color.GREEN)

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

    if Button.LEFT in pressed:
        now = watch.time()

        if now - light_pressed < 250:
            continue

        light_pressed = now

        light_level += 1
        light_level = light_level % len(light_cycle)
        brightness = light_cycle[light_level]

        if brightness == 0:
            light.off()
        else:
            light.on(brightness)
