# α EZDEV Devboard
A simple devboard using the Pi RP2040 for easier experimenting and development

So I decided to design my own Raspberry Pi Pico clone because, well, why not? It’s a fully functional RP2040 development board that runs all the standard firmware (MicroPython, CircuitPython, C/C++), but I upgraded the connector to USB-C because Micro-USB belongs in a museum.

## The Specs
* **Chip:** RP2040 (Dual-core M0+)
* **IO:** 30 GPIO pins broken out (just like the original)
* **Connector:** USB Type-C
* **Storage:** External Flash (QSPI)
* **Bling:** I replaced the boring single-color LED with a **WS2812B-2020 RGB LED** connected to **GPIO 25**.

## The Board

### PCB
<img width="384" height="674" alt="image" src="https://github.com/user-attachments/assets/cac41e1b-32eb-4628-97a6-f775104321c9" />

### PCB Front (3D Render)
<img width="515" height="532" alt="image" src="https://github.com/user-attachments/assets/f493041d-6e7e-4d8a-9ee0-7a848af7f27c" />

### PCB Back (3D Render)
<img width="801" height="536" alt="image" src="https://github.com/user-attachments/assets/aafb985f-0e46-4ae6-a548-e68bacd80dd0" />

### Schematic
<img width="1148" height="787" alt="image" src="https://github.com/user-attachments/assets/a26da800-f891-42d7-9333-e44f2f2d3aa0" />

## Firmware Note
Since I swapped the standard LED for a NeoPixel, you can't just toggle `GP25` high/low to blink it. You need to drive it as a single-pixel WS2812B strip on Pin 25.

**CircuitPython Example:**
```python
import board
import neopixel
pixel = neopixel.NeoPixel(board.GP25, 1)
pixel.fill((255, 0, 0)) # Red
```

### Credits
I didn't figure this all out by myself! This project was built following Kai Pierra's awesome guide on Hack Club Blueprint.

Check out the guide here: [Blueprint Starter Project: Devboard](https://blueprint.hackclub.com/starter-projects/devboard)
