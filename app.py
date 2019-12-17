import RPi.GPIO as GPIO
import time
import urllib2
#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BOARD)
#GPIO23
GPIO.setup(16, GPIO.OUT)
while True:
	htmlfile = urllib2.urlopen("https://iotguruhomeautomation.000webhostapp.com/buttonStatus.php")
    htmltext = htmlfile.read()
    print(htmltext)
    if (htmltext == b'S1ON'):
        GPIO.output(16, True)
        print ("LED ON")
        time.sleep(1)
    if (htmltext == b'S1OFF'):
        GPIO.output(16, False)
        print ("LED OFF")
        time.sleep(1)