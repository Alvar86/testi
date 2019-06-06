from microbit import *
import neopixel
import time

num_pixels = 24
pixels = neopixel.NeoPixel(pin0, num_pixels)
uart.init(baudrate = 115200)


def update_leds(r, g, b): # range 0-255
    global pixels
    for i in range (24):
        pixels[i] = (r, g, b)
        sleep(10) #ms
        pixels.show()
        

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b)

# rainbow animation
def rainbow_cycle(wait):
    global num_pixels
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep_ms(wait)

# bounce animation
def bounce(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(2 * num_pixels):
        for j in range(num_pixels):
            pixels[j] = (r, g, b)
        if (i // num_pixels) % 2 == 0:
            pixels[i % num_pixels] = (0, 0, 0)
        else:
            pixels[num_pixels - 1 - (i % num_pixels)] = (0, 0, 0)
        pixels.show()
        time.sleep_ms(wait)

#cycle animation
def cycle(r, g, b, wait):
    global pixels
    global num_pixels
    for i in range(num_pixels):
        for j in range(num_pixels):
            pixels[j] = (0, 0, 0)
        pixels[i % num_pixels] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# Almost same as update pixels
def colorWipe(r, g, b, wait):
    global pixels
    global pixes
    for j in range(num_pixels):
        pixels[j] = (r, g, b)
        pixels.show()
        time.sleep_ms(wait)

# rainbow function goes through colors
def rainbow(wait):
    global num_pixels
    global pixels
    for j in range(255):
        for i in range(num_pixels):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
            pixels.show()
        time.sleep_ms(wait)




while True:



    '''update_leds(255, 0, 0)
    sleep(2000)
    

    update_leds(0, 255, 0)
    sleep(2000)
    
    update_leds(0, 0, 255)
    time.sleep_ms(2000)'''
    
    message_bytes = uart.read()
    message = str(message_bytes)
    
    if  "a" in message:
        update_leds (255, 255, 255)
        
        print ('Lähetettiin komento a')
       
    elif  "b" in message:
        rainbow_cycle(5)
        print ('Lähetettiin komento b')
        
    elif  "c" in message:
        bounce(255, 0, 0, 5)
        print ('Lähetettiin komento c')
        
    update_leds(0, 0, 0)    
       




















