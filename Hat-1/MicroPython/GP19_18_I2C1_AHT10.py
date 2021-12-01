from machine import Pin, I2C
import utime
from time import sleep_ms


# Init I2C1 using pins GP19 & GP18
i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)
print (i2c)

#set normal mode
ackcnt = i2c.writeto(0x38, b'\xba') # b'10111010') #soft reset
print ("Reset ACK :", ackcnt)
sleep_ms(350)
ackcnt = i2c.writeto(0x38, b'\xe1') #b'11100001') #init cmd
print ("Init ACK :", ackcnt)
sleep_ms(100)
ackcnt = i2c.writeto(0x38, b'\xac') #b'10101100') #measure cmd
print ("Measure ACK :", ackcnt)
sleep_ms(350)

while True:
    ackcnt = i2c.writeto(0x38, b'\xac') #b'10101100') #measure cmd
    sleep_ms(350)
    data = i2c.readfrom(0x38, 6)

    temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
    ctemp = ((temp*200) / 1048576) - 50
    print("Temperature: {0:.1f}°C".format(ctemp))

    tmp = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4
    ctmp = int(tmp * 100 / 1048576)
    print("Humidity: {0}%".format(ctmp))
    sleep_ms(5000)



"""
#config = [0x08, 0x00]
#i2c.writeto_mem(0x38, 0xE1, config)
tmp = bytearray(2)
tmp[0] = 0x08
tmp[1] = 0x00
i2c.writeto_mem(0x38, 0xE1, tmp)
utime.sleep(0.5)

byt = i2c.readfrom_mem(0x38)
print(byt&0x68)
MeasureCmd = [0x33, 0x00]
i2c.writeto_mem(0x38, 0xAC, MeasureCmd)
time.sleep(0.5)

while True:
    data = i2c.readfrom_mem(0x38, 0x00)
    print(data)

    temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
    ctemp = ((temp*200) / 1048576) - 50
    print("Temperature: {0:.1f}°C".format(ctemp))

    tmp = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4
    ctmp = int(tmp * 100 / 1048576)
    print("Humidity: {0}%".format(ctmp))
"""