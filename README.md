PiIO
====

Raspberry Pi I/O Plate for Spike Relays and Switches

Innovation First or VEX H-Bridge Spike relays provide forward and reverse motor control for upto 16 volts at 10amps (http://www.vexrobotics.com/217-0220.html).
  
This custom Pi expansion plate and associated Python module allows up to 4 Spike relays to be controlled.  Additionally, 6 inputs are available for mechanical contact switches.

The nearly completed plate looks like this (it is just missing switch headers 5 and 6 in this photo).

![](https://raw.githubusercontent.com/FRC4564/PiIO/master/IOplate.jpg)


The plate fits Pi models B and B+. I used AdaFruits Raspberry Pi permaboard and their tall 26 pin header to connect into the GPIO lines and raise the board just above the USB ports. Needed a bit of electrical insulation on top of the USB ports so as not to short out the board.

There is no protection to the GPIO pins of the Pi in this design, so be careful what you connect and how.  The switch inputs are for mechanical contact switches only.  Don't connect anything that has power on them or you will likely fry your Pi (ouch!).

See the PDF file for the Pi Plate build layout. 

![](https://raw.githubusercontent.com/FRC4564/PiIO/master/protoboard.JPG)
