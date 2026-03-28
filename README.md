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

### BOMs
| Designator | Footprint | Quantity | Value | LCSC Part # |
| :--- | :--- | :--- | :--- | :--- |
| BT1 | PinHeader_1x02_P2.54mm_Vertical | 1 | Battery | DNP |
| C1, C10 | 402 | 2 | 1uF | [C52923](https://www.lcsc.com/search?q=C52923) |
| C11, C12, C17, C2, C3, C4, C5, C6, C7, C8, C9 | 402 | 11 | 0.1uF | [C1525](https://www.lcsc.com/search?q=C1525) |
| C13, C14 | 603 | 2 | 10uF | [C19702](https://www.lcsc.com/search?q=C19702) |
| C15, C16 | 402 | 2 | 33pF | [C1562](https://www.lcsc.com/search?q=C1562) |
| D1 | LED_WS2812B-2020_PLCC4_2.0x2.0mm | 1 | WS2812B-2020 | [C965555](https://www.lcsc.com/search?q=C965555) |
| J1 | USB_C_Receptacle_HRO_TYPE-C-31-M-12 | 1 | USB_C_Receptacle_USB2.0_14P | [C165948](https://www.lcsc.com/search?q=C165948) |
| J2, J3 | PinHeader_1x20_P2.54mm_Vertical | 2 | Conn_01x20 | DNP |
| J4 | PinHeader_1x03_P2.54mm_Vertical | 1 | Conn_01x03 | DNP |
| R1, R2 | 402 | 2 | 5.1K | [C25905](https://www.lcsc.com/search?q=C25905) |
| R3, R4 | 402 | 2 | 27 | [C25100](https://www.lcsc.com/search?q=C25100) |
| R5, R6 | 402 | 2 | 1K | [C11702](https://www.lcsc.com/search?q=C11702) |
| R7 | 402 | 1 | 10K | [C25744](https://www.lcsc.com/search?q=C25744) |
| R8 | 603 | 1 | 470R | [C114669](https://www.lcsc.com/search?q=C114669) |
| R9 | 603 | 1 | 2k | [C22977](https://www.lcsc.com/search?q=C22977) |
| SW1 | SW_Push_SPST_NO_Alps_SKRK | 1 | SW_Push | [C720477](https://www.lcsc.com/search?q=C720477) |
| U1 | QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm | 1 | RP2040 | [C2040](https://www.lcsc.com/search?q=C2040) |
| U2 | SOT-23 | 1 | MCP1700x-330xxTT | [C39051](https://www.lcsc.com/search?q=C39051) |
| U3 | SOT-23-5 | 1 | MCP73831-2-OT | [C14879](https://www.lcsc.com/search?q=C14879) |
| U4 | Winbond_USON-8-1EP_3x2mm_P0.5mm_EP0.2x1.6mm | 1 | W25Q16JVUXIQ TR | [C2843335](https://www.lcsc.com/search?q=C2843335) |
| Y1 | Crystal_SMD_3225-4Pin_3.2x2.5mm | 1 | 12 MHz | [C9002](https://www.lcsc.com/search?q=C9002) |
