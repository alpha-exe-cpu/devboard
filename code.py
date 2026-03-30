import board
import neopixel
import time

# Initialize the NeoPixel on GPIO 25
pixel = neopixel.NeoPixel(board.GP25, 1)

while True:
    # Set the LED to red
    pixel.fill((255, 0, 0))
    time.sleep(0.5)
    
    # Turn the LED off
    pixel.fill((0, 0, 0))
    time.sleep(0.5)
