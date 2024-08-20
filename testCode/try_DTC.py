import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


def main():

    dtc.refresh()

    dtc.check()

    dtc.display0()

    dtc.display1()

    dtc.display2()

    dtc.display3()

    dtc.display4()

    dtc.display5()

    dtc.display6()

    dtc.display7()

    dtc.display8()

    dtc.display9()


    GPIO.cleanup()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")
