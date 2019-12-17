import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 0
led2 = 0
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
@app.route('/')
def index():
    ledSts = GPIO.input(2)
    led2Sts = GPIO.input(3)
    templateData = { 'led' : led,
    'led2' : led2 }
    return render_template('index.html', **templateData)
@app.route('/<devicename>/<action>')
def do(deviceName, action):
    if deviceName == "led":
        actuator = 2
    if deviceName == "led2":
        actuator = 3
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    ledSts = GPIO.input(2)
    led2Sts = GPIO.input(3)
    templateData = { 'led' : 2,
    'led2' : 3 }
    return render_template('index.html', **templateData )
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)