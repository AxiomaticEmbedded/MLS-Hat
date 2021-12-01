from machine import Pin, PWM, Timer
import utime


din1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
din2 = Pin(1, Pin.IN, Pin.PULL_DOWN)


def din1_handler(pin):
    din1.irq(handler=None)
    utime.sleep_ms(100)
    if din1.value():
        print("DIN1 On !!!")
    din1.irq(handler=din1_handler)
    
def din2_handler(pin):
    din2.irq(handler=None)
    utime.sleep_ms(100)
    if din2.value():
        print("DIN2 On !!!")
    din2.irq(handler=din2_handler)

    
din1.irq(trigger=Pin.IRQ_RISING, handler=din1_handler)
din2.irq(trigger=Pin.IRQ_RISING, handler=din2_handler)

while True:
    utime.sleep(1)