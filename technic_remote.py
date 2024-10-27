from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Color, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.tools import wait, StopWatch

hub = TechnicHub()
remote = Remote()

try:
    motor_A = Motor(Port.A, Direction.CLOCKWISE)
except:
    motor_A = None

try:
    motor_B = Motor(Port.B, Direction.CLOCKWISE)
except:
    motor_B = None

try:
    motor_C = Motor(Port.C, Direction.CLOCKWISE)
except:
    motor_C = None

try:
    motor_D = Motor(Port.D, Direction.CLOCKWISE)
except:
    motor_D = None

watch = StopWatch()

hub.light.on(Color.GREEN)
remote.light.on(Color.GREEN)

motor_left = motor_A
motor_right = motor_B

power_left = 0
power_right = 0

while True:
    pressed = remote.buttons.pressed()

    if Button.CENTER in pressed:
        if motor_left == motor_A:
            motor_left = motor_C
            motor_right = motor_D
        else:
            motor_left = motor_A
            motor_right = motor_B

        if motor_left is not None:
            power_left = motor_left.speed()
        if motor_right is not None:
            power_right = motor_right.speed()

    if motor_left is not None and any(b in pressed for b in (Button.LEFT_PLUS, Button.LEFT_MINUS, Button.LEFT)):
        if Button.LEFT_PLUS in pressed:
            power_left += 100
        if Button.LEFT_MINUS in pressed:
            power_left -= 100
        if Button.LEFT in pressed:
            power_left = 0
        motor_left.run(power_left)

    if motor_right is not None and any(b in pressed for b in (Button.RIGHT_PLUS, Button.RIGHT_MINUS, Button.RIGHT)):
        if Button.RIGHT_PLUS in pressed:
            power_right += 100
        if Button.RIGHT_MINUS in pressed:
            power_right -= 100
        if Button.RIGHT in pressed:
            power_right = 0
        motor_right.run(power_right)

    wait(10)
