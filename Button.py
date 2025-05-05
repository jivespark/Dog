import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time
import RPi.GPIO as GPIO
i=1
# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define pins
BUTTON1_PIN = 17
BUTTON2_PIN = 27

# Setup buttons with pull-up resistors
GPIO.setup(BUTTON1_PIN, GPIO.IN)
    GPIO.setup(BUTTON2_PIN, GPIO.IN)

#  Set up I2C and OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Create blank image for drawing
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load default font
font = ImageFont.load_default()
#import image as frame1
D4 = Image.open("D4.png").convert("1")
D6 = Image.open("D6.png").convert("1")
D8 = Image.open("D8.png").convert("1")
D10 = Image.open("D10.png").convert("1")
D12 = Image.open("D12.png").convert("1")
D20 = Image.open("D20.png").convert("1")
def display_message(message):
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    draw.text((0, 25), message, font=font, fill=255)
    oled.image(image)
    oled.show()

# Initial display D4
display.image(D4)
display.show()
time.sleep(0.2)
try:
    while True:
        if i==1:
            display.image(D4)
            display.show()
            time.sleep(0.2)
        elif i==2:
            display.image(D6)
            display.show()
            time.sleep(0.2)
        elif i==3:
            display.image(D8)
            display.show()
            time.sleep(0.2)
        if i==4:
            display.image(D10)
            display.show()
            time.sleep(0.2)
        elif i==5:
            display.image(D12)
            display.show()
            time.sleep(0.2)
        elif i==6:
            display.image(D20)
            display.show()
            time.sleep(0.2)
        if GPIO.input(BUTTON1_PIN) == GPIO.HIGH:
            
        elif GPIO.input(BUTTON2_PIN) == GPIO.HIGH:
            
        else:
            time.sleep(0.02)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
