# Test Boot in ugit_test

import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixels.fill(0)
    time.sleep(0.2)
    pixels.fill(0x00F080)
    time.sleep(0.3)
