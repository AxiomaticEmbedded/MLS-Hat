from machine import Pin, ADC, UART, Timer
import utime

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

hc06 = UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(16), rx=Pin(17))


while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
#    print("Temperature : " + str(temperature) + "°C")
    
    data = "CPU Temperature = " + str(temperature) #+ "°C"
    txData = bytes(data, 'ascii')
    txData += '\n\r'
    hc06.write(txData)
    print (txData)
    utime.sleep (5)