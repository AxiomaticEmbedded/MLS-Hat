from machine import Pin, PWM
import utime

LED = 22

DRV1_STEP = 6
DRV1_DIR  = 7

DRV2_STEP = 8
DRV2_DIR  = 9

DRV3_STEP = 10
DRV3_DIR  = 11

DRV4_STEP = 12
DRV4_DIR  = 13

SPEED_VERY_FAST = 6500
SPEED_MORE_FAST = 5000
SPEED_FAST = 4000
SPEED_NORMAL = 3000
SPEED_SLOW = 15000
SPEED_VERY_SLOW = 1000

class DRV8825():
    def __init__(self, freq, FL_step, FL_dir, FR_step, FR_dir, RL_step, RL_dir, RR_step, RR_dir):
        self.FL_step = PWM(Pin(FL_step))
        self.FL_step.freq(freq)
        self.FL_dir = Pin(FL_dir, Pin.OUT)
        
        self.FR_step = PWM(Pin(FR_step))
        self.FR_step.freq(freq)
        self.FR_dir = Pin(FR_dir, Pin.OUT)

        self.RL_step = PWM(Pin(RL_step))
        self.RL_step.freq(freq)
        self.RL_dir = Pin(RL_dir, Pin.OUT)

        self.RR_step = PWM(Pin(RR_step))
        self.RR_step.freq(freq)
        self.RR_dir = Pin(RR_dir, Pin.OUT)
        
    def Direction(self, FL_dir, FR_dir, RL_dir, RR_dir):
        if (FL_dir) :
            self.FL_dir.value(1)
        else:
            self.FL_dir.value(0)

        if (FR_dir) :
            self.FR_dir.value(1)
        else:
            self.FR_dir.value(0)
            
        if (RL_dir) :
            self.RL_dir.value(1)
        else:
            self.RL_dir.value(0)
            
        if (RR_dir) :
            self.RR_dir.value(1)
        else:
            self.RR_dir.value(0)
           
    def Move(self, FL_step, FR_step, RL_step, RR_step):
        self.FL_step.duty_u16(FL_step)
        self.FR_step.duty_u16(FR_step)
        self.RL_step.duty_u16(RL_step)
        self.RR_step.duty_u16(RR_step)
            
    def Stop(self):
        self.FL_step.freq(0)
        self.FL_step.duty_u16(0)
        
        self.FR_step.freq(0)
        self.FR_step.duty_u16(0)
        
        self.RL_step.freq(0)
        self.RL_step.duty_u16(0)
        
        self.RR_step.freq(0)
        self.RR_step.duty_u16(0)
        
    def Forward(self):
        self.Direction(1, 1, 1, 1)
        
    def Backward(self):
        self.Direction(0, 0, 0, 0)
   
"""
# for Mecanum Wheel Use
    def leftTurn(self):
        
    def rightTurn(self):

    def leftRearTurn(self):
        
    def rightRearTurn(self):
        
    def leftshift(self):
        
    def rightshift(self):
    
    def leftforward45(self):
        
    def rightforward45(self):
        
    def leftbackward45(self):
        
    def rightbackward45(self):
"""

led = Pin(LED, Pin.OUT)

nema17 = DRV8825(1000, DRV1_STEP, DRV1_DIR, DRV2_STEP, DRV2_DIR, DRV3_STEP, DRV3_DIR, DRV4_STEP, DRV4_DIR)
print (nema17)

print ("Test Start")

for i in range (0, 5):
    led.value(1)
    
    print ("Try 5 times :", i+1)
    nema17.Forward()
    #nema17.Move(SPEED_SLOW, SPEED_SLOW, SPEED_SLOW, SPEED_SLOW)
    nema17.Move(SPEED_VERY_SLOW, SPEED_VERY_SLOW, 0, 0)
    utime.sleep(3)
    nema17.Stop()
    
    nema17.Backward()
    #nema17.Move(SPEED_SLOW, SPEED_SLOW, SPEED_SLOW, SPEED_SLOW)
    nema17.Move(SPEED_VERY_SLOW, SPEED_VERY_SLOW, 0, 0)
    utime.sleep(3)
    nema17.Stop()
    
led.value(0)
print ("Test End")
