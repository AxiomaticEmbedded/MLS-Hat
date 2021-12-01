from machine import Pin, PWM, Timer
import utime

up = Pin(6, Pin.IN, Pin.PULL_DOWN)
down = Pin(7, Pin.IN, Pin.PULL_DOWN)
select = Pin(8, Pin.IN, Pin.PULL_DOWN)

def up_handler(pin):
    up.irq(handler=None)
    utime.sleep_ms(100)
    if up.value():
        print("Up Button Pressed !!!")
    up.irq(handler=up_handler)

def down_handler(pin):
    down.irq(handler=None)
    utime.sleep_ms(100)
    if down.value():
        print("Down Button Pressed !!!")
    down.irq(handler=down_handler)
    
def select_handler(pin):
    select.irq(handler=None)
    utime.sleep_ms(100)
    if select.value():
        print("Select Button Pressed !!!")
    select.irq(handler=select_handler)
    
up.irq(trigger=Pin.IRQ_RISING, handler=up_handler)
down.irq(trigger=Pin.IRQ_RISING, handler=down_handler)
select.irq(trigger=Pin.IRQ_RISING, handler=select_handler)

while True:
    utime.sleep(5)