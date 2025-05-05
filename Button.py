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

# Load dice images
D4 = Image.open("D4.png").convert("1")
D6 = Image.open("D6.png").convert("1")
D8 = Image.open("D8.png").convert("1")
D10 = Image.open("D10.png").convert("1")
D12 = Image.open("D12.png").convert("1")
D20 = Image.open("D20.png").convert("1")

# List of dice images
dice_images = [D4, D6, D8, D10, D12, D20]

# Initial state
i = 0

try:
    while True:
        # Show current die image
        oled.image(dice_images[i])
        oled.show()

        # Button 1 (next die)
        if GPIO.input(BUTTON1_PIN) == GPIO.LOW:
            i = (i + 1) % len(dice_images)
            time.sleep(0.3)

        # Button 2 (previous die)
        elif GPIO.input(BUTTON2_PIN) == GPIO.LOW:
            i = (i - 1) % len(dice_images)
            time.sleep(0.3)

        time.sleep(0.02)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
