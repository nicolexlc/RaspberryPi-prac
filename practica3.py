import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)

gpio.setup(11,gpio.IN)
gpio.setup(7,gpio.OUT)

while True:
    button=gpio.input(11)
    print(button)
    if(button==1):
        gpio.output(7,True)
    else:
        gpio.output(7,False)

