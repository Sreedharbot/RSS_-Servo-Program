# Single Degree - Freedom Robotic Arm

Robotic Sensors & Signal Processing

This repo is for testing servo with raspberry pi 3b+ and uses python code for controlling the servo.

Things to do in this project are:

* Calibration Servo using Limit Switch
* Rotating 90° after Homing.
* Controlling the servo using potentiometer.
* Detecting objects using a Ultrasonic sensor.
* If the object is too close (Less than 15 cm) LED, should turn ON.
* If the object is too close, (Less than 15 cm) servo should be disabled while operating the potentiometer.
* When the potentiometer is "0" the servo should move to 0° and also should activate the LED indicating the servo reached 0°. 
* When the potentiometer is "1023" the servo should move to 90° and also should activate LED indicating the servo reached 90°.


To keep things neat. I made a case to place my components.

[Check out this like to print for case for yourself](https://www.printables.com/model/947881-raspberry-pi-3b-breadboard-case)


### This is the case 3D-model & design revision to 
![](https://media.printables.com/media/prints/947881/images/7237955_8b79199f-410a-4814-87b1-2dd7a014fc08_6ac41d04-9d1c-4499-8e8e-b1a93064cbe7/thumbs/inside/1920x1440/png/snipaste_2024-07-19_20-31-24.webp)

![](https://media.printables.com/media/prints/947881/images/7237991_b26a679d-451e-42dd-b50d-21b872e4777f_5044b605-af34-49bc-86f8-5b35085b0665/thumbs/inside/1920x1440/jpg/img20240719193845.webp)


## Wiring Diagram


![](https://i.pinimg.com/736x/d3/bf/21/d3bf218fb82d5beb6c1e342d02f19508.jpg)



## Flow Chart

![](https://i.pinimg.com/736x/f0/61/05/f061053d3bd1808bd88afe873a6ca855.jpg)



## Pin Configuration 

In this project, I have used the Raspberry Pi 3b+ model.

> **Note** : In Raspberry pi, you cannot drive **5V** OUTPUT/INPUT sensor (or) actuator.



Hardware :
* Raspberry Pi 3b+
* MCP3008 - ADC (Analog to Digital Convertor)
* Limit Switch
* Servo - SG90
* 10k Potentiometer 
* Ultrasonic Sensor (HC-SR04)
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
        Echo (Ultrasonic Sensor) -  |37    38| - LED ( 90° Position - OUTPUT)
                                    |39    40| - Trig (Ultrasonic Sensor)


These are the BMC pins of raspberry p, which means physical pins.

#### MCP3008 Pinouts - Pin Configuration 

        (Potentiometer) Channel 0 - |1      2| - 3.3V
                        Channel 1 - |3      4| - 3.3v
                        Channel 2 - |5      6| - GND
                        Channel 3 - |7      8| - Serial CLK 
                        Channel 4 - |9     10| - MISO 
                        Channel 5 - |11    12| - MOSI
                        Channel 6 - |13    14| - CS (Chip Select)
                        Channel 7 - |15    16| - GND