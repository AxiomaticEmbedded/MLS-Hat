from machine import Pin, ADC
import utime


# ADC0 (GP26)
adc0 = ADC(26)
# ADC1 (GP27)
adc1 = ADC(27)
# ADC2 (GP28)
adc2 = ADC(28)


while True:
    a0 = adc0.read_u16()
    a1 = adc1.read_u16()
    a2 = adc2.read_u16()
    
    data = "ADC0 = " + str(a0) + " ADC1 = " + str(a1) + " ADC2 = " + str(a2) + "\n"
    print (data)

    utime.sleep (1)