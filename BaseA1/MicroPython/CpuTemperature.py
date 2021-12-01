import machine
from machine import Pin, ADC, Timer
import utime

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

"""
tim = Timer()
def tick(timer):
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
#    print(temperature)
    print("Temperature : " + str(temperature) + "°C")
    
    freqValue = int(machine.freq() / 1000000)
    print("MCU Clock Speed : " + str(freqValue), " MHz")

tim.init(freq=5, mode=Timer.PERIODIC, callback=tick)
"""

freqValue = int(machine.freq() / 1000000)
print("MCU Clock Speed : " + str(freqValue), " MHz")

while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print("MCU Temperature : " + str(temperature) + "°C")
    
    utime.sleep(2)