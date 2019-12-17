from flask import Flask
app = Flask(__name__)
import os

@app.route("/gpio21/value/on")
def gpioValueSet(21, HIGH):
	cmd = 'echo {} > /sys/class/gpio/gpio{21}/value'.format(state, number)
	os.system(cmd)
	return "gpio{21} value set {HIGH}".format(number, state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)