# Vehicle-Telemetry-Script
Python script for UART serial communication with GPS module while parsing data packets for vehiclespeed and position using a Raspberry Pi 3

This was nessessary to reduce the strain on our PIU ATMega32M1 chips. Without this script and Rpi3 MCU, we overstrain the ATMega32M1 MCUs and lose periodically lose CAN and SPI communication functionality (very bad!).

---------------------------------------- GPS using UART on Raspberry Pi 3 ------------------------------

**all instructions for Windows 10 Pro** **refer to the last section of this document or imporant info** 
This program was created using the Raspberry Pi 3 (rpi3) with a heatsink on it, also know as the "rpisink" 
This means that all the edits to the config and cmdline files are done on the rpisink and NOT the rpi 
Below I have outlined the steps to get a blank rpi into a state where the GPS and the included code files will work

--------------------------------------- Connecting the GPS Module -------------------------------------

Refer to the pin diagrams inside the main folder: "GPIO Pin Layout Rpi3.jpg" and "GPS Pin Layout Rpi3.jpg"
1) Hook up GPS "VCC" pin to rpi3 "3V3" pin
2) Hook up GPS "GND" pin (either of them) to rpi3 "GND" pin
3) Hook up GPS "TX" pin to rpi3 "RX" pin
4) Plug the rpi3 into a computer/power source with a microUSB 

---------------------------------- SSH into your rpi3 using PuTTy and VNCVIEWER ------------------------

1) Follow *all the steps outline in the attached document: "SSH into Rpi3.pdf" 
 
* IF YOU ARE USING THE Raspberry Pi with a heatsink, change these steps!
   Part 1 Step 2: The SSID for the rpi with a heatsink is "rpisink", the password is the same "raspberry"

------------------------------------ Setting up the rpi for UART/Serial --------------------------------

Follow this guide step for step: https://wiki.dragino.com/index.php?title=Getting_GPS_to_work_on_Raspberry_Pi_3_Model_B

The same guide will help you test your GPS module. Make sure the GPS has a flashing red LED going off once you log into the rpi,
if you don't have a flashing red LED, then the GPS is not connected to enough satellights to work properly. This can be fixed by going 
outside (I know, what a pain) or working near a window. THIS WILL NOT WORK INSIDE HATCH! 


-------------------------------------- Running the GPS Parse Script -----------------------------------

* you must reset the baud rate to 57600 every time you boot the pi, or else you'll get corrupt results *

use this line in the pi terminal: sudo stty -F /dev/serial0 57600

If you want to see ALL GPS information with a nice GUI, copy and paste this file onto your rpi Desktop: long_gps.py
and then run these commands in terminal: 

python3 -m pip install -U pygame --user
cd Desktop 
sudo python ./long_gps.py

If you want to see ONLY position and time through terminal outputs, copy and paste this file onto your rpi Desktop: gps_parse.py
and then run these commands in terminal: 

cd Desktop 
sudo python ./gps_parse.py

-------------------------------------- Important Information ------------------------------------------

- GPS Documentation:  https://learn.sparkfun.com/tutorials/ls20031-5hz-66-channel-gps-receiver-hookup-guide
- On Raspberry Pi 3's, UART has been moved from ttyAMA0 to serial0. On the rpisink I edited some config/cmdline files to 
  make UART work on both serial0 AND ttyAMA0 so I could use older snipits of code on our rpi
- The GPS module we are using has a buad rate of 57600, if you don't change the baud rate everytime you boot the rpi then 
  the GPS data is going to be a big hunk of trash 
- I installed so many libraries I lost count, so if you try to run a script and an import statement failes, just download 
  the required library

![GPIO Pin Layout Rpi3](https://user-images.githubusercontent.com/36899160/113806429-1e1a1580-9717-11eb-820d-f4bb38f883a6.JPG)


