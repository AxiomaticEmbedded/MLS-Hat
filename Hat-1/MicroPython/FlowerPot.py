from machine import Pin, PWM, ADC, I2C, UART, Timer
import _thread

import utime

from DHT22 import DHT22
from SSD1306 import SSD1306_I2C
import framebuf


# AESLAB Stackable Hat-1 GPIO Used Pin List
UP_BTN     = 6
DOWN_BTN   = 7
SELECT_BTN = 8
DHT        = 9

LED        = 14
BUZZER     = 15

I2C0_SCL   = 21
I2C0_SDA   = 20
I2C1_SCL   = 19
I2C_SDA    = 20
UART0_RX   = 17
UART0_TX   = 16

ADC0       = 26
ADC1       = 27
ADC2       = 28


WIDTH  = 128   # oled display width
HEIGHT = 64    # oled display height

OLED_OFF_MINUTES = 3  

OLEDMode = 0   # OLED Power On/Off Mode

print ("FlowerPot Demo")
print ("")

# IO Device Setup 


up = Pin(UP_BTN, machine.Pin.IN, machine.Pin.PULL_DOWN)
down = Pin(DOWN_BTN, machine.Pin.IN, machine.Pin.PULL_DOWN)
select = Pin(SELECT_BTN, machine.Pin.IN, machine.Pin.PULL_DOWN)

dht22 = Pin(DHT, Pin.IN, Pin.PULL_UP)
dht22 = DHT22(dht22, Pin(DHT, Pin.OUT), dht11=False)
print (dht22)

led = Pin(LED, Pin.OUT)

buzzer = PWM(Pin(BUZZER))

adc0= ADC(ADC0)
adc1 = ADC(ADC1)
adc2 = ADC(ADC2)

# ADC CH4 is for RP2040 Internal Temperature Measure 
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)


# I2C0 - Init I2C using pins GP21 & GP20 
i2c0 = I2C(0, scl=Pin(I2C0_SCL), sda=Pin(I2C0_SDA), freq=400000)   
print("I2C Address      : "+hex(i2c0.scan()[0]).upper())# Display device address
print("I2C Configuration: "+str(i2c0))                  # Display I2C config

# Init oled display
oled = SSD1306_I2C(width=WIDTH, height=HEIGHT, i2c=i2c0, addr=0x3C, external_vcc=False) 
print (oled)

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)


# UART0 (HC-06 Bluetooth)
uart0 = UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(UART0_TX), rx=Pin(UART0_RX))
print (uart0)


print ("")
freqValue = int(machine.freq() / 1000000)
cf = "MCU C : " + str(freqValue) + " MHz"
print("MCU Clock : " + str(freqValue) + " MHz")
print ("")

wet_level = [0, 0, 0]

ct = ""
st = ""
t = ""
h = ""
z0 = ""
z1 = ""
z2 = ""

up = [330, 294, 262]
squidgame = [466, 622, 622, 0, 622, 0, 554, 0, 622, 622, 554, 466, 622]

def Buzzer0():
    print ("Buzzer Squid Game Play")
    for i in range(len(squidgame)):
        if (squidgame[i] == 0):
            buzzer.duty_u16(0)
        else:
            buzzer.duty_u16(19660)
            buzzer.freq(squidgame[i])
        utime.sleep(0.15)
    
    buzzer.duty_u16(0)
    
def Buzzer():
    print ("Buzzer Play")
    for i in range(len(up)):
        if (up[i] == 'P'):
            buzzer.duty_u16(0)
        else:
            buzzer.duty_u16(19660)
            buzzer.freq(up[i])
        utime.sleep(0.15)
    
    buzzer.duty_u16(0)

def uartSerialRxMonitor():
    recv = bytes()
    while uart0.any() > 0:
        recv += uart0.read(1)
#    res = recv.decode('utf-8')
    res = str(recv)
    res = res.upper()

    return res


def OLED_Off():
    global OLEDMode
    
    utime.sleep(OLED_OFF_MINUTES * 60) # 3 Minutes
    OLEDMode = 0
    oled.poweroff()
    Buzzer()
    print("Thread Expired > OLED Off !!!")
    

def select_handler(pin):
    global OLEDMode
    
    select.irq(handler=None)
    utime.sleep_ms(100)
    if select.value():
        print("Select Button Pressed > OLED On !!!")
        print ("")
        OLEDMode = 2
    select.irq(handler=select_handler)

def GetADC():
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range (0, 10) :
        a = adc0.read_u16()
        if a < 12000:
            a = 12001
        if a >= 18000:
            a = 18000
        data[i] = a
        utime.sleep(0.05)
        
    avg = sum(data)/len(data)
    avg -= 12000
    wet_level[0] = (int)(avg/1200) # (18000 - 12000)/5
    
    for i in range (0, 10) :
        a = adc1.read_u16()
        if a < 12000:
            a = 12000
        if a >= 18000:
            a = 18000
        data[i] = a
        utime.sleep(0.05)

    avg = sum(data)/len(data)
    avg -= 12000
    wet_level[1] = (int)(avg/1200) # (18000 - 12000)/5
    
    for i in range (0, 10) :
        a = adc2.read_u16()
        if a < 12000:
            a = 12000
        if a >= 18000:
            a = 18000
        data[i] = a
        utime.sleep(0.05)
        
    avg = sum(data)/len(data)
    avg -= 12000
    wet_level[2] = (int)(avg/1200) # (18000 - 12000)/5        
    

def Measure():
    global ct, st, t, h, z0, z1, z2
    
    led.value(1)
    print ("Measure :")
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = round((27 - ((reading - 0.706)/0.001721)), 1)
    ct = "MCU T : " + str(temperature) + " C"
    print ("\tMCU Temperature : " + str(temperature) + " °C")
    
    T, H = dht22.read()
    t = "T : " + str(T) + " C"  
    h = "H : " + str(H) + " %"
    st = t + " " + h
    print ("\tSystem Temperature : " + str(T) + " °C"  + " Humidity : " + str(H) + " °C")
    
    GetADC()
    
    z = "\t"
    z0 = "ADC0 : " + str(wet_level[0]) +  "/5"
    z1 = "ADC1 : " + str(wet_level[1]) +  "/5"
    z2 = "ADC2 : " + str(wet_level[2]) +  "/5"
    z += z0 + " " + z1 + " " + z2
    print (z)

    data = cf + "  " + ct + "  " + st + "  " + z0 + "  " + z1 + "  " + z2
    txData = bytes(data, 'ascii')
    txData += '\n\r'
    uart0.write(txData)
    print ("\tBT Msg : ", txData)
    led.value(0)
    print ("")
    
    
def MeasureTimer(timer):
    Measure()
    
    
select.irq(trigger=Pin.IRQ_RISING, handler=select_handler)

timer1 = Timer()
timer1.init(freq=0.05, mode=Timer.PERIODIC, callback=MeasureTimer)
# freq = 1 >> 1 / sec, 0.05 >> 1000 / 0.05 = 20000 means 20 sec period 
#timer1.init(freq=0.01, mode=Timer.PERIODIC, callback=MeasureTimer) # 100 sec period


OLEDMode = 1
_thread.start_new_thread(OLED_Off, ())

Buzzer0()
Measure()

CMD = "REQ"

while True:
    cmd = uartSerialRxMonitor()
    if CMD in cmd:
        data = cf + " " + ct + " " + st + " " + z0 + " " + z1 + " " + z2
        txData = bytes(data, 'ascii')
        txData += '\n\r'
        uart0.write(txData)
        print ("BT Msg by REQ : ", txData)
        
    if OLEDMode == 2:
        OLEDMode = 1
        oled.poweron()
        Buzzer()
        _thread.start_new_thread(OLED_Off, ())   
    
    if OLEDMode == 1:
        oled.fill(0)
        # Blit the image from the framebuffer to the oled display
        oled.blit(fb, 96, 20)

        oled.text(cf,                   1, 1)
        oled.text(ct,                   1, 9)
        oled.text(t,                    1,17)
        oled.text(h,                    1,25)
        oled.text(z0,                   1,33)
        oled.text(z1,                   1,41)
        oled.text(z2,                   1,49)
        oled.text("Oct. 2021 AESLAB",   1,57)
        oled.show()
    
    utime.sleep(0.5)

# END