# SmartBulbControlWithRaspberryPi

# Introduction
This is a small project made by me for the "Embedded systems" course from FCSE in Skopje. The goal of the project is to make the Raspberry Pi the central hub for controlling IoT devices in the home, such as smart doors, smart fridges etc. The Raspberry Pi can be accessed from a smartphone/tablet/laptop/PC. See the detailed information about the project below.
# Tools, Technologies and Equipment
For this project I was using the following tools, technologies and equipment:
- A Raspberry Pi 4 model B (2GB RAM)
- A Sense HAT add-on board for the Raspberry Pi, which can be used for getting various data such as temperature, humidity, barometric pressure etc. and also getting audiovisual feedback through the built-in 8x8 RGB LED matrix and connected speakers
- A LANBERG RGB smart bulb
- Blynk- A smartphone application that was used for controlling the devices on the network
- A smartphone to showcase the Blynk application and its use in the real world
- A laptop/PC to write the necessary Python code for the devices
- Visual Studio Code- used for connecting to the RPi via SSH and writing the necessary Python code
The BlynkApp.py file is the main file for running the application, while the BlynkTimer.py file is just a pre-made library function to be used for timeouts and timing intervals for the Sense HAT.
# BlynkApp
This is the main file for the application.
More information on how to obtain the parts mentioned below can be found on this link: https://pypi.org/project/tuya-bulb-control/
CLIENT_ID = ''
SECRET_KEY = ''
DEVICE_ID = ''
REGION_KEY = 'eu'

The rest of the code is pretty simple:
- The Blynk,BlynkTimer, Sense HAT functions are initialized 
- Virtual pins are being created for the buttons in the Blynk App
- Functions are defined for changing the color of the smart bulb, or just simply turning it on and off.
