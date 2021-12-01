from machine import Pin, I2C


i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)

print('Scan I2C0 Bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device !")
else:
    print('I2C devices found:',len(devices))

for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device)) 

print ("")

# Init I2C1 using pins GP19 & GP18
i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)    


print('Scan I2C1 Bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C1 device !")
else:
    print('I2C1 devices found:',len(devices))

for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))

