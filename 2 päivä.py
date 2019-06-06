
from microbit import *
import neopixel
import time

num_pixels = 24
pixels = neopixel.Neopixel(pin=0, num_pixels)


def update_leds(r, g, b): # range 0-255
    global pixels
    for i in range (24):
        pixels[i] = (r, g, b)
        sleep(10) #ms
        pixels.show()
        

while True:



    update_leds(255, 0, 0)
    time.sleep_ms(2000)
    

    update_leds(0, 255, 0)
    time.sleep_ms(2000)




















