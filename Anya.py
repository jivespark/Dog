import time
import board
import busio
import adafruit_ssd1306
from PIL import Image

# Setup I2C and display
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Load and convert both images to 1-bit format
frame1 = Image.open("IMG_3318.png").convert("1")
frame2 = Image.open("IMG_3316.png").convert("1")

# Animation loop
while True:
    display.image(frame1)
    display.show()
    time.sleep(0.2)

    display.image(frame2)
    display.show()
    time.sleep(0.2)
