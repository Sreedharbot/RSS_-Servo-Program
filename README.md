# RSS_-Servo-Program
Robot Signals & Sensors

This repo is for testing servo with raspiberry pi 3b+

I used python code for controlling the servo.

Things to do in this project are:

* Calibration Servo using Limit Swtich
* Rotating 90° after Homing.
* Controlling the servo using potentiometer.
* Detecting objects using ultrasonic sensor.
* If the object is too close (Less than 15cm) LED, should turn ON.
* If the object is too close, (Less than 15cm) servo should be disable while oprating the potentiometer.
* When the potentiometer is "0" the servo should move to 0° also should activate LED indicating servo reached 0°. 
* When the potentiometer is "1023" the servo should move to 90° also should activate LED indicating servo reached 90°.



## Wiring Diagram


![](https://i.pinimg.com/736x/d3/bf/21/d3bf218fb82d5beb6c1e342d02f19508.jpg)



## Flow Chart

![](https://i.pinimg.com/736x/f0/61/05/f061053d3bd1808bd88afe873a6ca855.jpg)



## Pin Configuration 

In this project, I have used Raspberry Pi 3b+ model.

> **Note** : In Raspberry pi, you cannot drive **5V** OUTPUT/INPUT sensor (or) actuator.



Hardware :
* Raspberry Pi 3b+
* MCP3008 - ADC (Analog to Digital Convertor)
* Limit Switch
* Servo - SG90
* 10k Potentiometer 
* Ultra-Sonic Sensor (HC-SR04)
* Red LED  
* Green LED
* Some Resistors (220E , 1K , 470E, 750E)


#### Raspberry Pi 3b+ Pinouts - Pin Configuration 

                             3.3V - |1      2| - 5V
                                    |3      4| - 5v
                                    |5      6| - GND
                                    |7      8| - Limit Switch (INPUT)
                                    |9     10| - LED (Human Detection - OUTPUT)
                                    |11    12| - Servo (PWM - OUTPUT)
                                    |13    14|
                                    |15    16|
                                    |17    18|
                      MOSI (SPI0) - |19    20|
                      MISO (SPI0) - |21    22|
                Serial CLK (SPI0) - |23    24| - CS (Chip Select - SPI0)
                                    |25    26|
                                    |27    28|
                                    |29    30|
                                    |31    32|
                                    |33    34|
                                    |35    36| - LED ( 0° Position - OUTPUT) 
        Echo (Ultra-Sonic Sensor) - |37    38| - LED ( 90° Position - OUTPUT)
                                    |39    40| - Trig (Ultra-Sonic Sensor)


#### MCP3008 Pinouts - Pin Configuration 

        (Potentiometer) Channel 0 - |1      2| - 3.3V
                        Channel 1 - |3      4| - 3.3v
                        Channel 2 - |5      6| - GND
                        Channel 3 - |7      8| - Serial CLK 
                        Channel 4 - |9     10| - MISO 
                        Channel 5 - |11    12| - MOSI
                        Channel 6 - |13    14| - CS (Chip Select)
                        Channel 7 - |15    16| - GND