from machine import Pin, PWM, I2C
import utime


MCP23008_nRESET = 5

PWMFL = 6
PWMFR = 7
PWMRL = 8
PWMRR = 9

_MCP23008_ADDR = 0x20

_MCP23008_IODIR    = 0x00
_MCP23008_IPOL     = 0x01
_MCP23008_GPINTEN  = 0x02     
_MCP23008_DEFVAL   = 0x03     
_MCP23008_INTCON   = 0x04     
_MCP23008_IOCON    = 0x05
_MCP23008_GPPU     = 0x06
_MCP23008_INTF     = 0x07     
_MCP23008_INTCAP   = 0x08     
_MCP23008_GPIO     = 0x09
_MCP23008_OLAT     = 0x0A


ALL_BRAKE = 0xFF
ALL_STOP = 0x00


class TB6612FNG():

    def __init__(self, mode, freq, rst):
        
        self. mode = mode
        
        nreset = Pin(rst, Pin.OUT)
        nreset.value(1)
        utime.sleep(0.01)
        nreset.value(0)
        utime.sleep(0.01)
        nreset.value(1)
        
        self.FL_pwm = PWM(Pin(PWMFL))
        self.FL_pwm.freq(freq) # freq Hz PWM
        self.FR_pwm = PWM(Pin(PWMFR)) 
        self.FR_pwm.freq(freq) # freq Hz PWM
        if self.mode == 2:     
            self.RL_pwm = PWM(Pin(PWMRL)) 
            self.RL_pwm.freq(freq) # freq Hz PWM
            self.RR_pwm = PWM(Pin(PWMRR)) 
            self.RR_pwm.freq(freq) # freq Hz PWM
        
        
        self.i2c = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)
        print (self.i2c)

        self.i2c_reg_write(_MCP23008_ADDR, _MCP23008_IODIR, 0x00)
        data = self.i2c_reg_read(_MCP23008_ADDR, _MCP23008_IODIR)
        print("EGP Dir : ", data)


    def Direction(self, dir):
        self.i2c_reg_write(_MCP23008_ADDR, _MCP23008_GPIO, dir)
        
    def Move(self, speed_FL=0, speed_FR=0, speed_RL=0, speed_RR=0):
        self.FL_pwm.duty_u16(speed_FL)
        self.FR_pwm.duty_u16(speed_FR)
        if self.mode == 2: 
            self.RL_pwm.duty_u16(speed_RL)
            self.RR_pwm.duty_u16(speed_RR) 

    def Stop(self):
        self.FL_pwm.duty_u16(0)
        self.FR_pwm.duty_u16(0)
        if self.mode == 2: 
            self.RL_pwm.duty_u16(0)
            self.RR_pwm.duty_u16(0)
            
        self.i2c_reg_write(_MCP23008_ADDR, _MCP23008_GPIO, ALL_STOP)
        data = self.i2c_reg_read(_MCP23008_ADDR, _MCP23008_GPIO)
        print("Wheel STOP : ", data)
            
    def Brake(self):
        self.FL_pwm.duty_u16(0)
        self.FR_pwm.duty_u16(0)
        if self.mode == 2: 
            self.RL_pwm.duty_u16(0)
            self.RR_pwm.duty_u16(0)
            
        self.i2c_reg_write(_MCP23008_ADDR, _MCP23008_GPIO, ALL_BRAKE)
        data = self.i2c_reg_read(_MCP23008_ADDR, _MCP23008_GPIO)
        print ("Wheel BRAKE :", data)
        
    def i2c_reg_write(self, addr, reg, data):
        # Construct message
        msg = bytearray()
        msg.append(data)
        
        # Write out message to register
        self.i2c.writeto_mem(addr, reg, msg)
        
    def i2c_reg_read(self, addr, reg, nbytes=1):
        # Check to make sure caller is asking for 1 or more bytes
        if nbytes < 1:
            return bytearray()
        
        # Request data from specified register(s) over I2C
        data = self.i2c.readfrom_mem(addr, reg, nbytes)
        
        return data

        
