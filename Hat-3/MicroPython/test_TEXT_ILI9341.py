from machine import Pin, SPI
import utime

from ILI9341 import ILI9341, color565


import glcdfont
import tt14
import tt24
#import tt32

# ILI9341 VCC, LED Pin Power 3.3V ... DIPSW No.2 On/Off
spi0 = SPI(0, baudrate=40000000, miso=Pin(4), mosi=Pin(3), sck=Pin(2))
display = ILI9341(spi0, cs=Pin(5), dc=Pin(1), rst=Pin(0), w=320, h=240, r=2)


fonts = [glcdfont,tt14,tt24]

text1 = 'abcdefghijklmnopqrstuvwxyz'
text2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text3 = '0123456789'


display.erase()
display.set_pos(0,0)

display.set_font(glcdfont)
display.print("glcdfont")
display.print(text1)
display.print(text2)
display.print(text3)
utime.sleep(1)

display.set_font(tt14)
display.print("tt14")
display.print(text1)
display.print(text2)
display.print(text3)
utime.sleep(1)

display.set_font(tt24)
display.print("tt24")
display.print(text1)
display.print(text2)
display.print(text3)
utime.sleep(1)

display.erase()
display.set_pos(0,0)
display.print ("End")


