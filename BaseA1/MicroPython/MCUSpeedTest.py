import machine, time

tus=time.ticks_us


machine.freq(10000000)                                                      
print("100 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())     
                                                              
machine.freq(133000000)                                                     
print("133 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())     
        
machine.freq(150000000)                                                     
print("150 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())

machine.freq(200000000)                                                     
print("200 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())

machine.freq(250000000)                                                     
print("250 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())

machine.freq(125000000)
print("125 MHz : ", -tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus(),-tus()+tus())