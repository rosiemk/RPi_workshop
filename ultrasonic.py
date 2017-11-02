import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

print("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# set trig pin low and give sensor time to settle
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

# Create trigger pulse (trig pin high for 10uS)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

# record last low timestamp for echo pin before return signal is received and pin goes high.
while GPIO.input(ECHO) == 0:
    pulse_start=time.time()

# echo received, pin goes high.  Get last high timestamp on echo pin
while GPIO.input(ECHO) == 1:
    pulse_end=time.time()

#calculate difference between two ie. duration of pulse
pulse_duration = pulse_end-pulse_start

#calculate distance (speed = distance/time) use 34300 for speed (/2=17150 for half distance)
distance = pulse_duration * 17150

# round to 2dp and print
distance = round(distance, 2)
print("Distance:",distance,"cm")

# reset pins
GPIO.cleanup()