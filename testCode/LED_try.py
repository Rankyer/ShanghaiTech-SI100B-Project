import RPi.GPIO as GPIO


LedPin = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, True)


try: 
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()
    print("")
