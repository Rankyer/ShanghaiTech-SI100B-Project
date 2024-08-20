import time
import digital_tube_control as dtc
import RPi.GPIO as GPIO


DCC = 7
A = 11
B = 12
C = 13
D = 15
E = 16
F = 18
G = 29
DP = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DCC, GPIO.OUT)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)

GPIO.output(DCC, True)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)
GPIO.output(E, True)
GPIO.output(F, False)
GPIO.output(G, False)
GPIO.output(DP, True)

time.sleep(3)

GPIO.cleanup()
