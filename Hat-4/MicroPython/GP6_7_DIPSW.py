from machine import Pin


dipsw1 = Pin(6, Pin.IN)
dipsw2 = Pin(7, Pin.IN)

print ("DIPSW : ", dipsw1.value(), dipsw2.value())