
from machine import Pin, Timer

led = Pin(22, Pin.OUT)

tim = Timer()
def tick(timer):
    led.toggle()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)

