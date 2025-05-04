import time
import board
import busio
import adafruit_ssd1306
from PIL import Image

# Setup I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Load all frames into a list
frames = []
for i in range(26):
    filename = f"frame{i:02}.png"
    image = Image.open(filename).convert("1")
    frames.append(image)

# Display the animation
while True:
    for frame in frames:
        display.image(frame)
        display.show()
        time.sleep(0.1)  # Adjust for frame speed