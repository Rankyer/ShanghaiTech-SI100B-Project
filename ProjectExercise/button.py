import RPi.GPIO as GPIO
from time import sleep
import pi_camera as pc


def setup():
    global BtnPin
    BtnPin = 31

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def detecting():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, bouncetime=250)
    while True:
        if GPIO.event_detected(BtnPin):
            return True


def getRespose(ev=None):
    print("Get Respose 1")


def event_detect():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=getRespose, bouncetime=250)

    print('Start detecting for 4s')

    while True:

        sleep(4)
        if GPIO.event_detected(BtnPin):
            print("Event detected\n")
        else:
            print("No event detected\n")

        sleep(1)
        GPIO.remove_event_detect(BtnPin)
        GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=getRespose, bouncetime=250)
        print("Restart detecting for GPIO.remove_event_detect(channel)4s")


def main():

    setup()

    event_detect()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
