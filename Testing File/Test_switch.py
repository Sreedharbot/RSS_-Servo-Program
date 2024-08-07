
import RPi.GPIO as GPIO
import time

button = 8

GPIO.setmode(GPIO.BOARD)

GPIO.setup(button,GPIO.IN, pull_up_down = GPIO.PUD_UP)


try:
	print("Press Ctrl+C to exit")
	while 1==1:

		button_state = GPIO.input(button)

		if not button_state:
			print("button is on")
		else:
			print("button is off")

except KeyboardInterrupt:
	print("\nExiting program")


finally:
		GPIO.cleanup()





