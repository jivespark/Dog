import time
import subprocess
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display
disp.fill(0)
disp.show()

# Create blank image for drawing
image = Image.new("1", (disp.width, disp.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while True:
    # Get system info (you can change this)
    output = subprocess.getoutput("uptime")

    # Clear image
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)

    # Draw output
    draw.text((0, 0), output[:disp.width//6], font=font, fill=255)

    # Display image
    disp.image(image)
    disp.show()
    time.sleep(2)
