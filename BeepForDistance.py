
import RPi.GPIO as GPIO
import time

class DistanceMeasurement(self):
    def __init__(self):
        self.TRIG = 23
        self.ECHO = 24
        self.PIEZO = 21
        self.distance = 0
        self.pulse_duration = 0

    def initialise_measurement():
        GPIO.setmode(GPIO.BCM)
        print ("Distance measurement in progress...")
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.setup(PIEZO, GPIO.OUT)
        time.sleep(2)
        GPIO.output(TRIG, False)

    def update():
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
            GPIO.output(PIEZO, True)
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            GPIO.output(PIEZO, False)
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 0)
        GPIO.output(TRIG, False)
        print ("Distance:",distance,"cm")
        time.sleep(min(max(0.025, distance/250), 2.5))

    def release():
        GPIO.cleanup()
