from machine import Pin, ADC
import utime



# ADC1 (GP26)
adc1 = ADC(26)
# ADC2 (GP27)
#adc2 = ADC(27)
# ADC3 (GP28)
#adc3 = ADC(28)

while True:
    a1 = adc1.read_u16()
#    a2 = adc2.read_u16()
#    a3 = adc3.read_u16()
    
    data = "ADC1 = " + str(a1) #+ " ADC2 = " + str(a2) + " ADC3 = " + str(a3) + "\n"
    print (data)
    utime.sleep (0.1)

