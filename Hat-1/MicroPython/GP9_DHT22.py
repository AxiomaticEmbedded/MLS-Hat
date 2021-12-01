from machine import Pin
import utime

from DHT22 import DHT22


dht22 = Pin(9, Pin.IN, Pin.PULL_UP)
dht22 = DHT22(dht22, Pin(9,Pin.OUT), dht11=False)

while True:
    T,H = dht22.read()
    if T is None:
        print(" sensor error")
    else:
        print("{:3.1f}°C  {:3.1f}%".format(T,H))
        
    #DHT22 not responsive if delay to short
    utime.sleep_ms(1000)
        
