import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route('/on')
def turn_led_on():
    GPIO.output(4, GPIO.HIGH)
    return "OK"

@app.route('/off')
def turn_led_off():
    GPIO.output(4, GPIO.LOW)
    return "OK"

if __name__ == '__main__':
    app.run()