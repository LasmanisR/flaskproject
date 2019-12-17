# main.py
import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)

@app.route('/on')
def turn_led_on():
    GPIO.output(ledPin, GPIO.HIGH)
    return "OK"

@app.route('/off')
def turn_led_off():
    GPIO.output(ledPin, GPIO.LOW)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')