import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

Servo_pin = 12

GPIO.setup(Servo_pin,GPIO.OUT)

frequency = 50

duty_cycle =1



try:



	pwm = GPIO.PWM(Servo_pin,frequency)


	pwm.start(duty_cycle)


	print(f"PWM runing on GPIO{Servo_pin} at {frequency} Hz with {duty_cycle}% duty cycle")
	input("press enter to stop")

except KeyboardInterrupt:
	print("\n Keyboard interrupt deteched")


finally:
	GPIO.cleanup()
	print("GPIO cleanup completed")
