from machine import Pin, PWM, ADC, I2C, SPI, Timer
import utime

from SSD1306 import SSD1306_I2C
from MFRC522 import MFRC522


# Pico vs RPi Pinmap
GPIO2 = 20
GPIO3 = 21
GPIO4 = 14

GPIO17 = 15
GPIO27 = 18
GPIO22 = 19

GPIO10 = 3
GPIO9 = 4
GPIO11 = 2

GPIO5 = 20
GPIO6 = 22
GPIO13 = 26
GPIO19 = 27
GPIO26 = 28

TxD = 16
RxD = 17
GPIO18 = 0

GPIO23 = 1
GPIO24 = 6

GPIO25 = 7
GPIO8 = 5
GPIO7 = 13

GPIO12 = 8

GPIO16 = 9
GPIO20 = 11
GPIO21 = 10

# AIUPL Used Pin
LED = GPIO4

DIPSW1 = GPIO17
DIPSW2 = GPIO27
DIPSW3 = GPIO22
DIPSW4 = GPIO7

BUZZER = GPIO16

CMD1 = GPIO20
CMD2 = GPIO21

TROUT1 = GPIO13
TROUT2 = GPIO19
TROUT3 = GPIO12

RELAY1 = GPIO12
RELAY2 = GPIO26

DIN1 = GPIO23
DIN2 = GPIO24


SDA = GPIO2
SCL = GPIO3

MFRC_RST = GPIO5
MFRC_IRQ = GPIO25
MFRC_MISO = GPIO9
MFRC_MOSI = GPIO10
MFRC_SCK = GPIO11
MFRC_SS = GPIO8


WIDTH  = 128          # 0.91" oled display width
HEIGHT = 32           # 0.91" oled display height


led = Pin(LED, Pin.OUT)
dipsw1 = Pin(DIPSW1, Pin.IN)
dipsw2 = Pin(DIPSW2, Pin.IN)
dipsw3 = Pin(DIPSW3, Pin.IN)
dipsw4 = Pin(DIPSW4, Pin.IN)

buzzer = Pin(BUZZER, Pin.OUT)
cmd1 = Pin(CMD1, Pin.IN)
cmd2 = Pin(CMD2, Pin.IN)
trout1 = Pin(TROUT1, Pin.OUT)
trout2 = Pin(TROUT2, Pin.OUT)
trout3 = Pin(TROUT3, Pin.OUT)
relay1 = Pin(RELAY1, Pin.OUT)
relay2 = Pin(RELAY2, Pin.OUT)
din1 = Pin(DIN1, Pin.IN)
din2 = Pin(DIN2, Pin.IN)

sda = Pin(SDA)
scl = Pin(SCL)

#rst = Pin(MFRC_RST, Pin.OUT)
#irq = Pin(MFRC_IRQ, Pin.IN)
#miso = Pin(MFRC_MISO, Pin.IN)
#mosi = Pin(MFRC_MOSI, Pin.OUT)
#sck = Pin(MFRC_SCK, Pin.OUT)
#ss = Pin(MFRC_SS, Pin.OUT)


def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring


trout1.value(1)

led.value(1)
buzzer.value(1)
relay1.value(1)
relay2.value(0)
utime.sleep(1.5)
led.value(0)
buzzer.value(0)
relay1.value(0)
relay2.value(1)

print ("DIPSW : ", dipsw1.value(), dipsw2.value(), dipsw3.value(), dipsw4.value())


sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
reading = sensor_temp.read_u16() * conversion_factor
temperature = 27 - (reading - 0.706)/0.001721
print("MCU Temperature : " + str(temperature) + "°C")

i2c = I2C(0, scl=scl, sda=sda, freq=400000)
print (i2c)

print('Scan I2C Bus...')
devices = i2c.scan()
if len(devices) == 0:
    print("No I2C device !")
else:
    print('I2C devices found:',len(devices))

for device in devices:
    print("Decimal address: ",device," | Hexa address: ", hex(device))
print ("")    

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
print (i2c)

oled = SSD1306_I2C(width=WIDTH, height=HEIGHT, i2c=i2c, addr=0x3C, external_vcc=False)  
print (oled)

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=5, rst=0)  
reader = MFRC522(spi_id=0, sck=MFRC_SCK, miso=MFRC_MISO, mosi=MFRC_MOSI, cs=MFRC_SS, rst=MFRC_RST)              
print ("MFRC522 RFID Reader :", reader)

PreviousCard = [0]

reader.init()
(stat, tag_type) = reader.request(reader.REQIDL)
print('request stat:',stat,' tag_type:',tag_type)
if stat == reader.OK:
    (stat, uid) = reader.SelectTagSN()
#    if uid == PreviousCard:
#        continue
    if stat == reader.OK:
        print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
        # All Data Dump
#        defaultKey = [255,255,255,255,255,255]
#        reader.MFRC522_DumpClassic1K(uid, Start=0, End=64, keyA=defaultKey)
#        print("Done")
        PreviousCard = uid
    else:
        print("No RFID Card")

text = "MCU T : "
command = ""

trout1.value(0)

def cmd1_handler(pin):
    global command
    
    cmd1.irq(handler=None)
    utime.sleep_ms(200)
    if cmd1.value():
        print("CMD1 On !!!")
        command = "CMD1 On"
#        buzzer.value(1)
#        utime.sleep_ms(100)
#        buzzer.value(0)
    cmd1.irq(handler=cmd1_handler)

def cmd2_handler(pin):
    global command
    
    cmd2.irq(handler=None)
    utime.sleep_ms(200)
    if cmd2.value():
        print("CMD2 On !!!")
        command = "CMD2 On"
#        buzzer.value(1)
#        utime.sleep_ms(100)
#        buzzer.value(0)
    cmd2.irq(handler=cmd2_handler)

def din1_handler(pin):
    global command
    
    din1.irq(handler=None)
    utime.sleep_ms(200)
    if din1.value():
        print("DIN1 On !!!")
        command = "DIN1 On"
#        buzzer.value(1)
#        utime.sleep_ms(100)
#        buzzer.value(0)
    din1.irq(handler=din1_handler)

def din2_handler(pin):
    global command
    
    din2.irq(handler=None)
    utime.sleep_ms(200)
    if din2.value():
        print("DIN2 On !!!")
        command = "DIN2 On"
#        buzzer.value(1)
#        utime.sleep_ms(100)
#        buzzer.value(0)
    din2.irq(handler=din2_handler)
    
cmd1.irq(trigger=Pin.IRQ_RISING, handler=cmd1_handler)
cmd2.irq(trigger=Pin.IRQ_RISING, handler=cmd2_handler)

din1.irq(trigger=Pin.IRQ_RISING, handler=din1_handler)
din2.irq(trigger=Pin.IRQ_RISING, handler=din2_handler)

while True:
    led.value(1)
        
    oled.fill(0)

    oled.text("AIUPL v1.0", 1, 1)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721, 2)
    oled.text(text+str(temperature), 1, 9)
    oled.text("CMD : " + command, 1, 17)
    oled.text("AESLAB", 1, 25)

    oled.show()
    
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(1)
    
"""
oled = SSD1306_I2C(width=WIDTH, height=HEIGHT, i2c=i2c, addr=0x3C, external_vcc=False)  
print (oled)

sensor = BME280(i2c=i2c)
print (sensor)

reader = MFRC522(spi_id=0, sck=sck, miso=miso, mosi=mosi, cs=ss, rst=rst)              
print ("MFRC522 RFID Reader :", reader)


def cmd1_handler(pin):
    cmd1.irq(handler=None)
    utime.sleep_ms(100)
    if cmd1.value():
        print("CMD1 On !!!")
        buzzer.value(1)
        utime.sleep_ms(300)
        buzzer.value(0)
    cmd1.irq(handler=cmd1_handler)

def cmd2_handler(pin):
    cmd2.irq(handler=None)
    utime.sleep_ms(100)
    if cmd2.value():
        print("CMD2 On !!!")
        buzzer.value(1)
        utime.sleep_ms(300)
        buzzer.value(0)
    cmd2.irq(handler=cmd2_handler)

def din1_handler(pin):
    din1.irq(handler=None)
    utime.sleep_ms(100)
    if din1.value():
        print("DIN1 On !!!")
        buzzer.value(1)
        utime.sleep_ms(300)
        buzzer.value(0)
    din1.irq(handler=din1_handler)

def din2_handler(pin):
    din2.irq(handler=None)
    utime.sleep_ms(100)
    if din2.value():
        print("DIN2 On !!!")
        buzzer.value(1)
        utime.sleep_ms(300)
        buzzer.value(0)
    din2.irq(handler=din2_handler)
    
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring


cmd1.irq(trigger=Pin.IRQ_RISING, handler=cmd1_handler)
cmd2.irq(trigger=Pin.IRQ_RISING, handler=cmd2_handler)

din1.irq(trigger=Pin.IRQ_RISING, handler=din1_handler)
din2.irq(trigger=Pin.IRQ_RISING, handler=din2_handler)

print ("AIUPL Run")
print ("")

buzzer.value(1)
utime.sleep(2)
buzzer.value(0)

ds1 = dipsw1.value()
ds2 = dipsw2.value()
ds3 = dipsw3.value()
ds4 = dipsw4.value()



print ("Mode : ", ds1, ds2, ds3, ds4)

freqValue = int(machine.freq() / 1000000)
print("MCU Clock Speed : " + str(freqValue), " MHz")
temp1 = "MCU C : {} MHz".format(freqValue)


while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    t1 = round(temperature, 2)
    temp = " T : {} C".format(t1)
    print(temp)
    
    
    t, p, h = sensor.read_compensated_data()

#    p = p // 256
#    pi = p // 100
#    pd = p - pi * 100

    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    
    v1 = "T : {} C".format(round((t / 100), 1))
#    v11 = "T : {}°C".format(round((t / 100), 1))
#    v2 = "P : {}.{:02d} hPa".format(pi, pd)
    v3 = "H : {}.{:02d} %".format(hi, hd)
    
    tmp = v1 + v3
    

    trout1.value(1)
    trout2.value(1)
    trout3.value(1)
    
    relay1.value(0)
    relay2.value(0)
    
    oled.fill(0)

    oled.text(temp1,1,1)
    oled.text(temp,80,1)
    oled.text(v1,1,9)
    oled.text(v3,64,9)

    oled.text("AESLAB AIUPL",10,17)

    oled.show()
    

    
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    #print('request stat:',stat,' tag_type:',tag_type)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if uid == PreviousCard:
            continue
        if stat == reader.OK:
            print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
# All Data Dump
#                defaultKey = [255,255,255,255,255,255]
#                reader.MFRC522_DumpClassic1K(uid, Start=0, End=64, keyA=defaultKey)
#
            print("Done")
            PreviousCard = uid
        else:
            pass
    else:
        PreviousCard=[0]
    
    trout1.value(0)
    trout2.value(0)
    trout3.value(0)
    
    relay1.value(1)
    relay2.value(1)
    
    utime.sleep(1)
""" 

