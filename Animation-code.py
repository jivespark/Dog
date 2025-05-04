import time
import board
import busio
import adafruit_ssd1306
from PIL import Image

# Setup display
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Load the sprite sheet (should be 3328x64 for 26 frames)
sprite_sheet = Image.open("IMG_3319.png").convert("1")

# Cut and display frames
frame_width = 128
frame_height = 64
num_frames = 26

while True:
    for i in range(num_frames):
        # Crop the frame from the sheet
        box = (i * frame_width, 0, (i + 1) * frame_width, frame_height)
        frame = sprite_sheet.crop(box)
        
        # Show frame
        display.image(frame)
        display.show()
        time.sleep(0.1)