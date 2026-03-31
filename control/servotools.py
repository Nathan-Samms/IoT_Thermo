from time import sleep

from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from settings import MAX_ANGLE_UI, MIN_ANGLE_UI, PW_MAX, PW_MIN, SERVO_GPIO

MIN_ANG = -90
MAX_ANG = 90

class servoController():
    def __init__(self, pin=SERVO_GPIO):
        self.factory = PiGPIOFactory()
        self.servo = AngularServo(
            pin,
            min_pulse_width = PW_MIN,
            max_pulse_width = PW_MAX,
            min_angle = MIN_ANG,
            max_angle = MAX_ANG,
            pin_factory = self.factory
        )

        def set_angle(self, angle):
            a = max(MIN_ANGLE_UI, min(MAX_ANGLE_UI, float(angle)))
            internal = a - 90.0
            self.servo.angle = internal
            self.last = a
            sleep(0.02)
            return self.last
        
        def get_last(self):
            return self.last
        
        def off(self):
            self.servo.angle = None

servo = servoController()

