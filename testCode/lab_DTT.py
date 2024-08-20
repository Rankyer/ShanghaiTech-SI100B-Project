import RPi.GPIO as GPIO
import time


DCC = 7
A = 11
B = 12
C = 13
D = 15
E = 16
F = 18
G = 32
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
GPIO.output(A, True)
GPIO.output(B, True)
GPIO.output(C, True)
GPIO.output(D, True)
GPIO.output(E, True)
GPIO.output(F, True)
GPIO.output(G, True)
GPIO.output(DP, True)

time.sleep(10)

GPIO.cleanup()