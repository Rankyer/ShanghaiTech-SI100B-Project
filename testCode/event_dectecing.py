import RPi.GPIO as GPIO
from time import sleep


BtnPin = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BtnPin, GPIO.IN)
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getRespose(ev=None):
    print("get Respose 1")


GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=getRespose, bouncetime=250)


print('start detecting for 4s')

while True:
    sleep(4)
    if GPIO.event_detected(BtnPin):
        print("Event detected\n")
    else:
        print("No event detected\n")

    sleep(1)
    print("Restart detecting for 4s")