import asyncio
import RPi.GPIO as GPIO
import numpy as np
import time

swt_pin = 8
servo_pin = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(swt_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)

class Eventhandler:
    def __init__(self):
        self.zero = 0
        self.home_angle = 0
        self.position = 0


    def rot_angle(self,i):
        angle = max(0,min(180,i))
        duty_cycle = 1 + (9/180)*angle
        est = round(duty_cycle,1)
        return est

    async def servo(self):

        for i in range(0,190,10):
            a = self.rot_angle(i)
            pwm.ChangeDutyCycle(a)
            print(i)
            print(a)
            time.sleep(1)
            limit_status = GPIO.input(swt_pin)
            if not limit_status:
                print("Servo is at 0°")
                #pwm.stop()
                self.zero = a
                self.home_angle = i
                print(f"The dutycycle is {self.zero} & the angle is {self.home_angle}")
                break
        await asyncio.sleep(1)


    async def servo_rotate(self):
        self.position = self.home_angle-100
        print(f'home angle is {self.home_angle} & position is {self.position}')
        for i in range(self.home_angle,self.position,-10):
            a = self.rot_angle(i)
            pwm.ChangeDutyCycle(a)
            print(self.home_angle-i)
            print(a)              #pulse-width signal
            time.sleep(1)
        await asyncio.sleep(1)



    # async def limit():
        
    #     limit_status = GPIO.IN(swt_pin)

    #     if not limit_status:
    #        await print("Servo is at 0°")

    async def shutdown(self):
        pwm.stop()
        GPIO.cleanup

    async def main(self):
        await self.servo()
        await self.servo_rotate()
        #await limit()
        await self.shutdown()


handler = Eventhandler()
asyncio.run(handler.main())
