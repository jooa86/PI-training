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
pwr = GPIO.PWM(pwrLedPin, 50)

# Initial state for LEDs
GPIO.output(statusLedPin, GPIO.low)
pwm.start(dutyCycle);
print("Up and running! Press CTRL+C to exit")
