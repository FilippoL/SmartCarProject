
import RPi.GPIO as GPIO
import time

class DistanceMeasurement:
    def __init__(self):
        self.TRIG = 23
        self.ECHO = 24
        self.PIEZO = 21
        self.distance = 0
        self.pulse_duration = 0

    def initialise(self):
        GPIO.setmode(GPIO.BCM)
        print ("Distance measurement in progress...")
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.setup(self.PIEZO, GPIO.OUT)
        time.sleep(2)
        GPIO.output(self.TRIG, False)

    def update(self):
        GPIO.output(self.TRIG,True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO) == 0:
            GPIO.output(self.PIEZO, True)
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            GPIO.output(self.PIEZO, False)
            pulse_end = time.time()

        self.pulse_duration = pulse_end - pulse_start
        self.distance = self.pulse_duration * 17150
        self.distance = round(self.distance, 0)
        GPIO.output(self.TRIG, False)
        print ("Distance:",self.distance,"cm")
        time.sleep(min(max(0.025, self.distance/250), 2.5))

    def release(self):
        GPIO.cleanup()
