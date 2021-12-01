from machine import Pin, I2C
from micropython import const
import utime

from BME280 import BME280

i2c1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)
print (i2c1)
sensor = BME280(i2c=i2c1)
print (sensor)
print ("")

#print (sensor.values())
while True:
    t, p, h = sensor.read_compensated_data()

    p = p // 256
    pi = p // 100
    pd = p - pi * 100

    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    print ("{}°C".format(t / 100), "{}.{:02d}hPa".format(pi, pd), "{}.{:02d}%".format(hi, hd))
  
    utime.sleep(2)
    
"""
from machine import Pin, I2C
import utime


from BME280 import BME280


i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
print (i2c0)
bme280 = BME280(i2c=i2c0)
print (bme280)

print (bme280.temperature())
print (bme280.humidity())
"""