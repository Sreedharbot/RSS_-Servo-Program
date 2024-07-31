
#Authur: Sreedhar RP
#Creation Date: 27-07-2024

#Libraries Added
import asyncio
import RPi.GPIO as GPIO
import numpy as np
import time
import spidev
import os
import sys


#Global Varibles 
Led = 10
swt_pin = 8
servo_pin = 12
Trig = 40
echo = 37


#implementation of the SPI communication with MCP3008
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000 #Commmunication frequency, recommened in the datasheet

#RPi board pin & mode declaration.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(swt_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(Led,GPIO.OUT)
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)


#using handler to execute the task.
class Eventhandler:
    def __init__(self):
        self.zero = 0
        self.home_angle = 0
        self.position = 0


    def rot_angle(self,i):                          # Function used to Change Angles to Duty Cycle
        angle = max(0,min(180,i))                   # Seting the range.
        duty_cycle = 1 + (9/180)*angle
        est = round(duty_cycle,1)
        return est

    def pot_value(self,channel):
        command = [1,(8+channel<<4),0]                  #Enabling SPI Communication.
        response = spi.xfer2(command)                   #Making a Hand-shake between RPi and MCP3008
        adc_value = ((response[1]&3)<<8)+response[2]    #requestion 10bit adc value
        return adc_value


    async def servo(self):                              #Async Function for calibarating servo.
        for i in range(0,190,10):
            a = self.rot_angle(i)                       
            pwm.ChangeDutyCycle(a)
            limit_status = GPIO.input(swt_pin)
            #print(i)
            #print(a)
            time.sleep(0.1)
            if not limit_status:                        # Detecting Collision in the limit swtich.
                print("Servo is at 0°")
                #pwm.stop()
                self.zero = a
                self.home_angle = i
                print(f"The dutycycle is {self.zero} & the angle is {self.home_angle}°")
                break
        await asyncio.sleep(0.3)


    async def servo_rotate(self):                       #Rotating 90° after homing
        self.position = self.home_angle-100
        print(f'home angle is {self.home_angle} & position is {self.position}')
        for i in range(self.home_angle,self.position,-10):
            a = self.rot_angle(i)
            pwm.ChangeDutyCycle(a)
            print(self.home_angle-i)
            #print(a)                                    #pulse-width signal
            time.sleep(0.1)
        await asyncio.sleep(0.3)

    async def potentiometer(self):                      #Using Pot to control the Servo 
        while True:
            value = self.pot_value(0)
            new_angle = (90/1023)*value               
            b = self.rot_angle(new_angle)
            pwm.ChangeDutyCycle(b)
            if value>0:
                print(f"ADC value from the pot {value} & the servo position is {new_angle}")
            await asyncio.sleep(0.1)

            GPIO.output(Trig,False)                    #activating the Ultrasonic sensor to detect object 
            #print("sensoring setting")
            time.sleep(0.3)
            GPIO.output(Trig,True)
            time.sleep(0.00001)
            GPIO.output(Trig,False)


            while GPIO.input(echo)==0:
                start_time = time.time()
            
            while GPIO.input(echo)==1:
                end_time = time.time()

            time_duration = end_time-start_time

            distance = time_duration*17150
            distance = round(distance,2)
            status = GPIO.input(swt_pin)

            if distance<=15:                                #if the object is less thanm 15c, the red LED turns ON
                GPIO.output(Led,True)
                print(f"Object detected distance: {distance} cm")
                print(f"Servo is stopped , Press the limit swtich to active")
                value = 0
                pwm.stop()
                
            elif not status:
                print(f"button status {status} ")
                print("Restarting the Program")
                GPIO.cleanup()
                python = sys.executable 
                script = os.path.abspath(__file__)
                os.execl(python, python, script, *sys.argv)


            else:
                GPIO.output(Led,False)
            

    async def shutdown(self):
        pwm.stop()
        GPIO.cleanup

    async def main(self):                   #All the functions are executed from the main() function
        await self.servo()
        await self.servo_rotate()
        await self.potentiometer()
        #await limit()
        await self.shutdown()


try:
    handler = Eventhandler()
    asyncio.run(handler.main())

except KeyboardInterrupt:                   #Keyboardinterrupt to exit the code, with clering the GPIOs per-defined condtions 
    pwm.stop()
    GPIO.cleanup()
    print("Closing the program")