from machine import Pin, I2C
import utime


reset = Pin(5, Pin.OUT)
reset.value(1)
utime.sleep(0.1)
reset.value(0)
utime.sleep(0.1)
reset.value(1)

_MCP23008_ADDR = 0x20

_MCP23008_IODIR    = 0x00
_MCP23008_IPOL     = 0x01
_MCP23008_GPINTEN  = 0x02     # INT
_MCP23008_DEFVAL   = 0x03     # INT
_MCP23008_INTCON   = 0x04     # INT
_MCP23008_IOCON    = 0x05
_MCP23008_GPPU     = 0x06
_MCP23008_INTF     = 0x07     # INT
_MCP23008_INTCAP   = 0x08     # INT
_MCP23008_GPIO     = 0x09
_MCP23008_OLAT     = 0x0A

IODIR              = 0x80

i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)
print (i2c)

def reg_write(i2c, addr, reg, data):
    # Construct message
    msg = bytearray()
    msg.append(data)
    
    # Write out message to register
    i2c.writeto_mem(addr, reg, msg)
    
def reg_read(i2c, addr, reg, nbytes=1):
    # Check to make sure caller is asking for 1 or more bytes
    if nbytes < 1:
        return bytearray()
    
    # Request data from specified register(s) over I2C
    data = i2c.readfrom_mem(addr, reg, nbytes)
    
    return data

data = reg_read(i2c, _MCP23008_ADDR, _MCP23008_IODIR)
print(data)

#data = int.from_bytes(data, "big") | (1 << 3)
reg_write(i2c, _MCP23008_ADDR, _MCP23008_IODIR, 0x00)

data = reg_read(i2c, _MCP23008_ADDR, _MCP23008_IODIR)
print(data)

reg_write(i2c, _MCP23008_ADDR, _MCP23008_GPIO, 0xAB)

data = reg_read(i2c, _MCP23008_ADDR, _MCP23008_GPIO)
print(data)

