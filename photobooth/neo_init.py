import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D21, 64)

pixels.fill((0, 0, 0))

# TOP
pixels[0] = (255, 0, 0)
pixels[1] = (255, 32, 0)
pixels[2] = (255, 64, 0)
pixels[3] = (255, 96, 0)
pixels[4] = (255, 128, 0)
pixels[5] = (255, 160, 0)
pixels[6] = (255, 192, 0)
pixels[7] = (255, 225, 0)

# RIGHT
pixels[15] = (192, 255, 0)
pixels[23] = (160, 255, 0)
pixels[31] = (128, 255, 0)
pixels[39] = (96, 255, 0)
pixels[47] = (64, 255, 0)
pixels[55] = (32, 255, 0)

# BOTTOM
pixels[63] = (0, 255, 0)
pixels[62] = (0, 255, 32)
pixels[61] = (0, 255, 64)
pixels[60] = (0, 255, 96)
pixels[59] = (0, 255, 128)
pixels[58] = (0, 255, 160)
pixels[57] = (32, 255, 192)
pixels[56] = (64, 255, 225)

# LEFT
pixels[48] = (128, 160, 160)
pixels[40] = (160, 128, 128)
pixels[32] = (192, 96, 96)
pixels[24] = (225, 64, 64)
pixels[16] = (225, 32, 32)
pixels[8] = (225, 0, 0)

time.sleep(3)
pixels.fill((0, 0, 0))
