from machine import Pin, ADC
import utime

adc0 = ADC(26)
adc1 = ADC(27)
adc2 = ADC(28)

conversion_factor = 3.3 / 65535


# Will return a integer
def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def map(val, loval, hival, tolow, tohigh):
     if loval <= val <= hival:
         return (val - loval)/(hival-loval)*(tohigh-tolow) + tolow
     else:
         raise(ValueError)

def map1(s, a1, a2, b1, b2):
     return int(b1 + (s - a1) * (b2 - b1) / (a2 - a1))
    
def avg_adc():
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(0, 9):
        a0 = adc0.read_u16()
        _a0 = a0 * conversion_factor 
        var[i] = _a0
        utime.sleep (0.03)
        
    sum = 0
    for i in range(0, 9):
        sum = sum + var[i]
        
    result = int(sum/10)
    return result         
   
   
while True: 
    #var = avg_adc()
    a0 = adc0.read_u16()
    _a0 = a0 * conversion_factor
    __a0 = map1(_a0, 0.0, 3.3, 1, 100)
    
    a1 = adc1.read_u16()
    _a1 = a1 * conversion_factor
    __a1 = map1(_a1, 0.0, 3.3, 1, 100)
    
    a2 = adc2.read_u16()
    _a2 = a2 * conversion_factor
    __a2 = map1(_a2, 0.0, 3.3, 1, 100)
    
    
#    data = "ADC0 = " + str(__a0) + " ADC1 = " + str(__a1) + " ADC2 = " + str(__a2) + "\n"
    data = "ADC0 = " + str(__a0) + "\n" 
    print (data)
    utime.sleep (0.5)

