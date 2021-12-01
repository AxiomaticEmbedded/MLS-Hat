from machine import Pin, PWM
import utime

servo1 = PWM(Pin(14))
servo2 = PWM(Pin(15))
 
#servo3 = PWM(Pin(22))
#servo4 = PWM(Pin(26))
#servo5 = PWM(Pin(27))
#servo6 = PWM(Pin(28))     

servo1.freq(50)
servo2.freq(50)

#servo3.freq(50)
#servo4.freq(50)
#servo5.freq(50)
#servo6.freq(50)


MIN = 2000 
MID = 6000 
MAX = 8000 

servo1.duty_u16(MID)
servo2.duty_u16(MIN)
utime.sleep(1)


cnt1 = MIN
dir1 = 0
while True:
    servo1.duty_u16(cnt1)
    utime.sleep(0.5)
    servo2.duty_u16(cnt1)
    utime.sleep(0.5)
    if dir1 == 0:
        cnt1 = cnt1 + 1000
        if cnt1 >= 8000:
            cnt1 = 8000
            dir1 = 1
    else:
        cnt1 = cnt1 - 1000
        if cnt1 <= 2000:
            cnt1 = 2000
            dir1 = 0

"""
while True:

    print ("Servo #1")
    servo1.duty_ns(MIN)
    utime.sleep(1)
    
    servo1.duty_ns(MID)
    utime.sleep(1)
    
    servo1.duty_ns(MAX)
    utime.sleep(1)



    print ("Servo #2")
    servo2.duty_ns(MIN)
    utime.sleep(1)
    
    servo2.duty_ns(MID)
    utime.sleep(1)
    
    servo2.duty_ns(MAX)
    utime.sleep(1)
"""
