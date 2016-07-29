import RPi.GPIO as GPIO
import time

# Settings
pwrLedPin = 18
statusLedPin = 23
buttonPin = 17
dutyCycle = 95

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwrLedPin, GPIO.OUT)
GPIO.setup(statusLedPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm = GPIO.PWM(pwrLedPin, 50)

# Initial state for LEDs
GPIO.output(statusLedPin, GPIO.LOW)
pwm.start(dutyCycle);
print("Up and running! Press CTRL+C to exit")

try:
    while 1:
        if GPIO.input(buttonPin): # button released
            pwm.ChangeDutyCycle(dutyCycle)
            GPIO.output(statusLedPin, GPIO.LOW)
        else: # button pressed
            pwm.ChangeDutyCycle(100 - dutyCycle)
            GPIO.output(statusLedPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(statusLedPin, GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt: #If CTRL+C is pressed
    pwm.stop()
    GPIO.cleanup()
