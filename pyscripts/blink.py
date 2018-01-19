# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(1.0)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup() # cleanup all GPIO
            
