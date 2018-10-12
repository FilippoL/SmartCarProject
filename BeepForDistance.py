
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
PIEZO = 21
print ("Distance measurement in progress...")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(PIEZO,GPIO.OUT)
time.sleep(2)
GPIO.output(TRIG, False)

while True:
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
    
GPIO.cleanup()