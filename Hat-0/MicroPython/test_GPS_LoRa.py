from machine import Pin, UART, SPI, Timer
import utime

from GPS import GPS

from LORA import LORA


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

# GPS-LoRa Used Pin
TX = TxD
RX = RxD

LORA_RST = GPIO27
LORA_DIO = GPIO18
LORA_MISO = GPIO6
LORA_MOSI = GPIO5
LORA_SCK = GPIO13
LORA_nSS = GPIO12


tx = Pin(TX)
rx = Pin(RX)

rst = Pin(LORA_RST, Pin.OUT)
lora_irq = Pin(LORA_IRQ, Pin.IN)
miso = Pin(LORA_MISO, Pin.IN)
mosi = Pin(LORA_MOSI, Pin.OUT)
sck = Pin(LORA_SCK, Pin.OUT)
ss = Pin(LORA_SS, Pin.OUT)


gps = GPS(uart=0, tx=tx, rx=rx, baud=9600)
print (gps)

lora = LORA(spi_id=0, sck=sck, miso=miso, mosi=mosi, cs=ss, rst=rst, irq=lora_irq)              
print (lora)


print ("GPS/LoRa Run")
print ("")


while True:

    data = gps.read()
    print (data)
    
    lora.send(data)
 
    utime.sleep(1)
    

