from machine import Pin, Timer
import utime


tr1 = Pin(18, Pin.OUT)
tr2 = Pin(19, Pin.OUT)
tr3 = Pin(22, Pin.OUT)

"""
tim = Timer()
def tick(timer):
    tr1.toggle()
    tr2.toggle()
    tr3.toggle()
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
"""

while True:
    tr1.value(1)
    utime.sleep(0.2)
    tr1.value(0)
    
    tr2.value(1)
    utime.sleep(0.2)
    tr2.value(0)
    
    tr3.value(1)
    utime.sleep(0.2)
    tr3.value(0)
