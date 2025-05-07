import board
import busio
from PIL import Image
import adafruit_ssd1306

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# OLED display dimensions (adjust if needed)
WIDTH = 128
HEIGHT = 64

# Create the display instance
display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear display
display.fill(0)
display.show()

# Load image
image = Image.open("IMG_3372.png").convert("1")  # Convert to 1-bit monochrome

# Resize image to fit the display
image = image.resize((WIDTH, HEIGHT))

# Display the image
display.image(image)
display.show()