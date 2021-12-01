
from machine import Pin, Timer

board_led = Pin(25, Pin.OUT)

tim = Timer()
def tick(timer):
    board_led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

