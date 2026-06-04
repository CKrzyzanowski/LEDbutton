
from flask import Flask
from gpiozero import gpiozero

led = LED(17)
button = Button(2)

button.when_pressed = led.toggled

print ("led toggled press ctr + c to exit ")

pause()
