import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

print("Distance measurement in progress")

#set GPIO direction (in/out)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print("...")
def distance ():
    # set trig to HIGH
    GPIO.output(TRIG, True)
    
    # after 0.01ms set trig to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    # save start time
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
        
    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
        
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with sonic speed (34300 cm/s)
    # and divide by 2 because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("%.1f" % dist)
            time.sleep(0.5)
        
        # reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
