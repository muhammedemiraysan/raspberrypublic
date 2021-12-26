import Adafruit.GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst = RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1',(width,height))
draw = ImageDraw.Draw(image)
draw.rectangle((1,1,width,height),outline = 0,fill = 0 )
padding = -2
top = padding
bottom = height-padding
x = 0
buyuk = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.tff",15)
orta = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.tff",12)
kucuk = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.tff",10)
font = ImageFont.load_default()
draw.text((35,top),"test",font=buyuk,fill=255)
while(True):
    disp.image(image)
    disp.display()
