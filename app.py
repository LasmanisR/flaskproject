import RPi.GPIO as GPIO



class PiThings(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def read_button(self):
        return GPIO.input(4)

    def set_led(self, value):
        GPIO.output(17, value)