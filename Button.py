import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time
import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pins
BUTTON1_PIN = 17
BUTTON2_PIN = 27

# Setup buttons with pull-up resistors
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Create blank image for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load default font
font = ImageFont.load_default()

def display_message(message):
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    draw.text((0, 25), message, font=font, fill=255)
    oled.image(image)
    oled.show()

# Initial screen
display_message("Waiting for input...")

try:
    while True:
        if GPIO.input(BUTTON1_PIN) == GPIO.LOW:
            display_message("Button 1 pressed")
            time.sleep(0.2)
        elif GPIO.input(BUTTON2_PIN) == GPIO.LOW:
            display_message("Button 2 pressed")
            time.sleep(0.2)
        else:
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()