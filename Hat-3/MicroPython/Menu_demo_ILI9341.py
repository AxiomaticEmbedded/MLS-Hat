# MIT License; Copyright (c) 2017 Jeffrey N. Magee

from machine import Pin, PWM, SPI
import utime
import _thread

from ILI9341 import ILI9341, color565


import glcdfont
import tt14
import tt24
#import tt32

# ILI9341 VCC, LED Pin Power 3.3V ... DIPSW No.2 On/Off
spi0 = SPI(0, baudrate=40000000, miso=Pin(4), mosi=Pin(3), sck=Pin(2))
display = ILI9341(spi0, cs=Pin(5), dc=Pin(1), rst=Pin(0), w=320, h=240, r=2)

up = Pin(6, Pin.IN, Pin.PULL_DOWN)
down = Pin(7, Pin.IN, Pin.PULL_DOWN)
select = Pin(8, Pin.IN, Pin.PULL_DOWN)


# With Stackable Hat-1 LED & Buzzer
led = Pin(14, Pin.OUT)
buzzer = PWM(Pin(15))


list = ["Menu 1", "Menu 2", "Menu 3"]

curr_menu = 0
select_mode = 0

# We create a semaphore
semaphore = _thread.allocate_lock()


tones = {
    '0':    1,
    'B0':  31,
    'C1':  33,
    'CS1': 35,
    'D1':  37,
    'DS1': 39,
    'E1':  41,
    'F1':  44,
    'FS1': 46,
    'G1':  49,
    'GS1': 52,
    'A1':  55,
    'AS1': 58,
    'B1':  62,
    'C2':  65,
    'CS2': 69,
    'D2':  73,
    'DS2': 78,
    'E2':  82,
    'F2':  87,
    'FS2': 93,
    'G2':  98,
    'GS2': 104,
    'A2':  110,
    'AS2': 117,
    'B2':  123,
    'C3':  131,
    'CS3': 139,
    'D3':  147,
    'DS3': 156,
    'E3':  165,
    'F3':  175,
    'FS3': 185,
    'G3':  196,
    'GS3': 208,
    'A3':  220,
    'AS3': 233,
    'B3':  247,
    'C4':  262,
    'CS4': 277,
    'D4':  294,
    'DS4': 311,
    'E4':  330,
    'F4':  349,
    'FS4': 370,
    'G4':  392,
    'GS4': 415,
    'A4':  440,
    'AS4': 466,
    'B4':  494,
    'C5':  523,
    'CS5': 554,
    'D5':  587,
    'DS5': 622,
    'E5':  659,
    'F5':  698,
    'FS5': 740,
    'G5':  784,
    'GS5': 831,
    'A5':  880,
    'AS5': 932,
    'B5':  988,
    'C6':  1047,
    'CS6': 1109,
    'D6':  1175,
    'DS6': 1245,
    'E6':  1319,
    'F6':  1397,
    'FS6': 1480,
    'G6':  1568,
    'GS6': 1661,
    'A6':  1760,
    'AS6': 1865,
    'B6':  1976,
    'C7':  2093,
    'CS7': 2217,
    'D7':  2349,
    'DS7': 2489,
    'E7':  2637,
    'F7':  2794,
    'FS7': 2960,
    'G7':  3136,
    'GS7': 3322,
    'A7':  3520,
    'AS7': 3729,
    'B7':  3951,
    'C8':  4186,
    'CS8': 4435,
    'D8':  4699,
    'DS8': 4978,
}

# Melody
start = ['E4','D4','C4']
song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]



def playtone(duty, frequency):
    buzzer.duty_u16(duty)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def StartPlay():
    for i in range(len(start)):
        if (start[i] == "P"):
            bequiet()
        else:
            playtone(19660, tones[start[i]])
        utime.sleep(0.15)
    bequiet()
    
    display.set_color(fg=red, bg=black)        
    display.fill_rectangle(0, 100, 319, 24)
    _thread.exit()

def SongPlay():
    for i in range(len(song)):
        if (song[i] == "P"):
            bequiet()
        else:
            playtone(1000, tones[song[i]])
        utime.sleep(0.3)
    bequiet()
    
    display.set_color(fg=red, bg=black)        
    display.fill_rectangle(0, 100, 319, 24)
    _thread.exit()

def LED():
    global select_mode
    
    while True:
        if select_mode == 1:
            led.value(1)
            utime.sleep(0.3)
            led.value(0)
            utime.sleep(0.2)
        else:
            break
    
    display.set_color(fg=red, bg=black)        
    display.fill_rectangle(0, 100, 319, 24)
    _thread.exit()

        
display.erase()
display.set_pos(20, 0)
display.set_font(tt14)
display.print("Stackable Hat-3 ILI9341 (240x320)")

white = color565(255, 255, 255)
black = color565(0, 0, 0)
red = color565(255, 0, 0)
green = color565(0, 255, 0)
blue = color565(0, 0, 255)




def menu_run():
    global select_mode
    

    if select_mode == 1:
        display.set_color(fg=red, bg=black) 
        display.fill_rectangle(0, 100, 319, 24)
        display.set_pos(40,100)
        display.set_font(tt24)
        display.set_color(fg=red, bg=green)
        txt = "Execute " + str(list[curr_menu])
        display.print(txt)
        
        if curr_menu == 0:
            _thread.start_new_thread(LED, ())
        if curr_menu == 1:
            _thread.start_new_thread(StartPlay, ())
        if curr_menu == 2:
            _thread.start_new_thread(SongPlay, ())
        
    
def menu_display():
    display.set_pos(0,15)
    display.set_font(tt24)
    for i in range(len(list)):
        display.set_color(fg=white, bg=green)
        if curr_menu == i :
            display.set_color(fg=blue, bg=green)
        txt = str(list[i])
        display.print(txt)


def up_handler(pin):
    global curr_menu
    
    up.irq(handler=None)
    utime.sleep_ms(100)
    if up.value():
        curr_menu = curr_menu - 1
        if curr_menu < 0:
            curr_menu = 0
        menu_display()
#        txt = "Up " + str(curr_menu)
#        print (txt)
    up.irq(handler=up_handler)

def down_handler(pin):
    global curr_menu
    
    down.irq(handler=None)
    utime.sleep_ms(100)
    if down.value():
        curr_menu = curr_menu + 1
        if curr_menu > 2:
            curr_menu = 2
        menu_display()
#        txt = "Down " + str(curr_menu)
#        print (txt)
    down.irq(handler=down_handler)
    
def select_handler(pin):
    global select_mode
    
    select.irq(handler=None)
    utime.sleep_ms(100)
    if select.value():
        if select_mode == 0:
            select_mode = 1
            menu_run()
        else:
            select_mode = 0
                
#    txt = "Select " + str(curr_menu)
#    print (txt)        
    select.irq(handler=select_handler)
    
up.irq(trigger=Pin.IRQ_RISING, handler=up_handler)
down.irq(trigger=Pin.IRQ_RISING, handler=down_handler)
select.irq(trigger=Pin.IRQ_RISING, handler=select_handler)


menu_display()
while True:
#    semaphore.acquire()
    utime.sleep(1)
#    semaphore.release()

