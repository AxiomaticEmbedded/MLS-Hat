import utime

from TB6612FNG import TB6612FNG
    

FL_FORWARD = 0x01
FL_BACKWARD = 0x02
FL_STOP = 0x00
FL_BREAK = 0x03

FR_FORWARD = 0x01 << 2
FR_BACKWARD = 0x02 << 2
FR_STOP = 0x00 << 2
FR_BREAK = 0x03 << 2

RL_FORWARD = 0x01 << 4
RL_BACKWARD = 0x02 << 4
RL_STOP = 0x00 << 4
RL_BREAK = 0x03 << 4

RR_FORWARD = 0x01 << 6
RR_BACKWARD = 0x02 << 6
RR_STOP = 0x00 << 6
RR_BREAK = 0x03 << 6


SPEED_VERY_FAST = 65000
SPEED_MORE_FAST = 50000
SPEED_FAST = 40000
SPEED_NORMAL = 30000
SPEED_SLOW = 20000

MCP23008_nRESET = 5

print ("Test Start")

mtr = TB6612FNG(mode = 2, freq=100, rst=MCP23008_nRESET)     # TB6612FNG_1 and TB6612FNG_2 Use 
#mtr = TB6612FNG(mode = 1, freq=100, rst=MCP23008_nRESET)      # TB6612FNG_1 Use Only
print (mtr)
print ("")

mtr.Stop()
mtr.Brake()

print ("Forwad")
mtr.Direction(FL_FORWARD | FR_FORWARD | RL_FORWARD | RR_FORWARD)
#mtr.Direction(FL_FORWARD | FR_FORWARD)
mtr.Move(SPEED_NORMAL, SPEED_NORMAL, SPEED_NORMAL, SPEED_NORMAL)
#mtr.Move(SPEED_SLOW, SPEED_NORMAL, 0, 0)
utime.sleep(5)
mtr.Stop()

utime.sleep(1)

print ("Backward")
mtr.Direction(FL_BACKWARD | FR_BACKWARD | RL_BACKWARD | RR_BACKWARD)
#mtr.Direction(FL_BACKWARD | FR_BACKWARD)
speed = SPEED_SLOW
mtr.Move(SPEED_NORMAL, SPEED_NORMAL, SPEED_NORMAL, SPEED_NORMAL)
#mtr.Move(SPEED_NORMAL, SPEED_SLOW, 0, 0)
utime.sleep(5)
mtr.Stop()

mtr.Brake()
print ("Test End")



"""
print ("Front Left Wheel...Forward")
mtr.direction(0x01)

FL = PWM(Pin(PWMFL))
#FL.duty_u16(65000)
FL.duty_u16(20000)
FL.freq(100)
utime.sleep(5)
FL.duty_u16(0)

print ("Front Left Wheel...Backward")
mtr.direction(0x02)

FL = PWM(Pin(PWMFL))
#FL.duty_u16(65000)
FL.duty_u16(20000)
FL.freq(100)
utime.sleep(5)
FL.duty_u16(0)


print ("Front Right Wheel...Forward")
mtr.direction(0x01 << 2)

FR = PWM(Pin(PWMFR))
#FR.duty_u16(65000)
FR.duty_u16(20000)
FR.freq(100)
utime.sleep(5)
FR.duty_u16(0)

print ("Front Right Wheel...Backward")
mtr.direction(0x02 << 2)

FR = PWM(Pin(PWMFR))
#FR.duty_u16(65000)
FR.duty_u16(20000)
FR.freq(100)
utime.sleep(5)
FR.duty_u16(0)
"""

"""
print ("...Forward")
#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_FORWARD | FL_FORWARD)

speed = 800
#mtr.move(speed, speed, speed, speed)
mtr.move(speed, speed, 0, 0)

utime.sleep(5)


print ("...Backward")
#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_BACKWARD | FL_BACKWARD)
#mtr.move(speed, speed, speed, speed)

speed = 300
mtr.move(speed, speed, 0, 0)
utime.sleep(5)


print ("...Left")
#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_FORWARD | FL_FORWARD)

speed = 500
#mtr.move(speed, speed, speed, speed)
mtr.move(speed, int(speed*1.5), 0, 0)
utime.sleep(5)


print ("...Right")
#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_FORWARD | FL_FORWARD)

speed = 500
#mtr.move(speed, speed, speed, speed)
mtr.move(int(speed*1.5), speed, 0, 0)
utime.sleep(5)



print ("...Break")
speed = 0
#mtr.move(speed, speed, speed, speed)
mtr.move(speed, speed, 0, 0)

#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_BRAKE | FL_BRAKE)



print ("...Stop")
speed = 0
#mtr.move(speed, speed, speed, speed)
mtr.move(speed, speed, 0, 0)

#mtr.dir(RR_FORWARD | RL_FORWARD | FR_FORWARD | FL_FORWARD)
mtr.dir(FR_STOP | FL_STOP)
"""



