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
    ledZSts = GPIO.input(2)
    ledSSts = GPIO.input(3)
    templateData = { 'ledZ' : led,
    'ledS' : led2 }
    return render_template('index.html', **templateData)
@app.route('/<devicename>/<action>')
def do(deviceName, action):
    if deviceName == "ledZ":
        actuator = 2
    if deviceName == "ledS":
        actuator = 3
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
    ledZSts = GPIO.input(2)
    ledSSts = GPIO.input(3)
    templateData = { 'ledZ' : 2,
    'ledS' : 3 }
    return render_template('index.html', **templateData )
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)