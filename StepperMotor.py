import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DIR = 7
STEP = 8
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

DIR2 = 21
STEP2 = 20
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)


while  True:
    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.LOW)
    sleep(0.1)
    for i in range(0,100):
            GPIO.output(STEP2, GPIO.HIGH)
            GPIO.output(STEP, GPIO.HIGH)
            sleep(0.002)
            GPIO.output(STEP2, GPIO.LOW)
            GPIO.output(STEP, GPIO.LOW)
            sleep(0.002)
    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR2, GPIO.HIGH)
    sleep(0.1)
    for i in range(0,100):
            GPIO.output(STEP2, GPIO.HIGH)
            GPIO.output(STEP, GPIO.HIGH)
            sleep(0.005)
            GPIO.output(STEP2, GPIO.LOW)
            GPIO.output(STEP, GPIO.LOW)
            sleep(0.005)
