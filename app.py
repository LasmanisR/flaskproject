Learn more or give us feedback
from flask import Flask
app = Flask(__name__)
import os


@app.route("/gpio21/direction/out")
def gpioDirectionRead(number):
	cmd = 'cat /sys/class/gpio/gpio{21}/direction'.format(number)
	direction = os.popen(cmd).read()
	return "gpio{21} direction == {out}".format(number, direction)


@app.route("/gpio21/value/off")
def gpioValueRead(number):
	cmd = 'cat /sys/class/gpio/gpio{21}/value'.format(number)
	state = os.popen(cmd).read()
	return "gpio{21} value == {LOW}".format(number, state)

@app.route("/gpio21/value/on")
def gpioValueSet(number, state):
	cmd = 'echo {} > /sys/class/gpio/gpio{21}/value'.format(state, number)
	os.system(cmd)
	return "gpio{21} value set {HIGH}".format(number, state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)