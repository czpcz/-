import time,board,digitalio,serial,pulseio
from loongpio import LED
from time import sleep
import threading

def key():
    if btn.value:
        print("no")
    else:
        print("yes")
def uart1(serial):
    while True:
        data=serial.read_all()
        if data=='':
            continue
        else:
            break
        sleep(0.02)
    return data
def uart2():
    data=uart1(serial)
    if data!=b'' :
        print("receive:",data)
        serial.write(data)
        if data==b'0x01\r\n':
            led1.on()
        if data==b'0x02\r\n':
            led1.off()
def PWMa():#you
    while True:
        if btn.value==1 and btn1.value==0 and btn2.value==0:
            for i in range(100):
                if i<50:
                    p11.duty_cycle=int(i*2*65535/100)
                else:
                    p11.duty_cycle=65535-int((i-50)*2*65535/100)
            time.sleep(0.01)
        if btn.value==1 and btn1.value==1 and btn2.value==0:
            time.sleep(4)
            for i in range(100):
                if i<50:
                    p11.duty_cycle=int(i*2*65535/100)
                else:
                    p11.duty_cycle=65535-int((i-50)*2*65535/100)
        if btn.value==0:
            time.sleep(6)
            for i in range(100):
                if i<50:
                    p11.duty_cycle=int(i*2*65535/100)
                else:
                    p11.duty_cycle=65535-int((i-50)*2*65535/100)
            time.sleep(0.01)
def PWMb():
    while True:     
        if btn.value==1 and btn1.value==0 and btn2.value==0:
            for i in range(100):
                if i<50:
                    p22.duty_cycle=int(i*2*65535/100)
                else:
                    p22.duty_cycle=65535-int((i-50)*2*65535/100)
            
        if btn.value==1 and btn1.value==0 and btn2.value==1:
            time.sleep(4)
            for i in range(100):
                if i<50:
                    p22.duty_cycle=int(i*2*65535/100)
                else:
                    p22.duty_cycle=65535-int((i-50)*2*65535/100)
        

p11=pulseio.PWMOut(board.PWM0,frequency=5000,duty_cycle=5000)
p22=pulseio.PWMOut(board.PWM1,frequency=5000,duty_cycle=5000)
btn=digitalio.DigitalInOut(board.GPIO2)
btn.direction=digitalio.Direction.INPUT

btn1=digitalio.DigitalInOut(board.GPIO38)  
btn1.direction=digitalio.Direction.INPUT

btn2=digitalio.DigitalInOut(board.GPIO41)   
btn2.direction=digitalio.Direction.INPUT


led1=LED(7)
led2=LED(1)
led2.on()
led3=LED(4)

serial=serial.Serial('/dev/ttyUSB0',115200,timeout=0.5)
if serial.isOpen():
    print("open success")
else:
    print("open false")

if __name__=='__main__':
    p1=threading.Thread(target=PWMa)
    p2=threading.Thread(target=PWMb)
    p1.start()
    p2.start()
    while True:
        key()
        data=uart1(serial)
        uart2()
