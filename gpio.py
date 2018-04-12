import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(18, 50)

MAX = 10.0 # percent
MID = 7.5
MIN = 5 # percent

servo.start(MID)

try:
    while True:
        servo.ChangeDutyCycle(MIN)
        time.sleep(2)
        servo.ChangeDutyCycle(MAX)
        time.sleep(2)
        servo.ChangeDutyCycle(MID)
        time.sleep(2)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

