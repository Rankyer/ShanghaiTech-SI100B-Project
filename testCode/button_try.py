import RPi.GPIO as GPIO
import time


def main():

    setup()

    detecting()


def setup():

    global BtnPin
    BtnPin = 31

    global LedPin
    LedPin = 33

    global Led_status
    Led_status = False


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, False)


def swLED(ev=None):

    global Led_status
    Led_status = not Led_status

    GPIO.output(LedPin, Led_status)

    if Led_status == False:
        print('LED Off')

    else:
        print('LED On')


def detecting():

    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLED, bouncetime=250)

    while True:
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
