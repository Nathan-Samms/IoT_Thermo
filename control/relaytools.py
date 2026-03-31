import RPi.GPIO as GPIO
from settings import RELAY_PIN
from state import state

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(RELAY_PIN, GPIO.OUT)


def fan_on():
    GPIO.output(RELAY_PIN, GPIO.LOW)
    state.set_fan(True)

def fan_off():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    state.set_fan(False)

def fan_state():
    """Returns True = ON, False = OFF"""
    return state.get_fan() 

fan_off()
