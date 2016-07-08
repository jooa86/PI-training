import RPi.GPIO as GPIO

print "GPIO Testing..."

GPIO.setmode(GPIO.BOARD)
GPIO.setup(4, GPIO.OUT)
GPIO.output(7, True)
