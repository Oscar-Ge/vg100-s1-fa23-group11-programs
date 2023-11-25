# DC_motor - By: 13407 - 周五 11月 24 2023

import sensor, image, time
import machine
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

lcd.init(freq=15000000)


p1=machine.Pin(,machine.Pin.OUT) #front left
p2=machine.Pin(,machine.Pin.OUT) #front left
p3=machine.Pin(,machine.Pin.OUT) #front right
p4=machine.Pin(,machine.Pin.OUT) #front right
p5=machine.Pin(,machine.Pin.OUT) #back left
p6=machine.Pin(,machine.Pin.OUT) #back left
p7=machine.Pin(,machine.Pin.OUT) #back right
p8=machine.Pin(,machine.Pin.OUT) #back right



def forward:
    pwm1=machine.PWM(p1)
    pwm1.freq(38000)
    pwm1.duty(1000)
    pwm2=machine.PWM(p2)
    pwm2.freq(38000)
    pwm2.duty(0)
    pwm3=machine.PWM(p3)
    pwm3.freq(38000)
    pwm3.duty(1000)
    pwm4=machine.PWM(p4)
    pwm4.freq(38000)
    pwm4.duty(0)
    pwm5=machine.PWM(p5)
    pwm5.freq(38000)
    pwm5.duty(1000)
    pwm6=machine.PWM(p6)
    pwm6.freq(38000)
    pwm6.duty(0)
    pwm7=machine.PWM(p7)
    pwm7.freq(38000)
    pwm7.duty(1000)
    pwm8=machine.PWM(p8)
    pwm8.freq(38000)
    pwm8.duty(0)



def backward:
    pwm1=machine.PWM(p1)
    pwm1.freq(38000)
    pwm1.duty(0)
    pwm2=machine.PWM(p2)
    pwm2.freq(38000)
    pwm2.duty(100)
    pwm3=machine.PWM(p3)
    pwm3.freq(38000)
    pwm3.duty(0)
    pwm4=machine.PWM(p4)
    pwm4.freq(38000)
    pwm4.duty(100)
    pwm5=machine.PWM(p5)
    pwm5.freq(38000)
    pwm5.duty(0)
    pwm6=machine.PWM(p6)
    pwm6.freq(38000)
    pwm6.duty(100)
    pwm7=machine.PWM(p7)
    pwm7.freq(38000)
    pwm7.duty(0)
    pwm8=machine.PWM(p8)
    pwm8.freq(38000)
    pwm8.duty(100)





def turnright:
    pwm1=machine.PWM(p1)
    pwm1.freq(38000)
    pwm1.duty(1000)
    pwm2=machine.PWM(p2)
    pwm2.freq(38000)
    pwm2.duty(0)
    pwm3=machine.PWM(p3)
    pwm3.freq(38000)
    pwm3.duty(100)
    pwm4=machine.PWM(p4)
    pwm4.freq(38000)
    pwm4.duty(0)
    pwm5=machine.PWM(p5)
    pwm5.freq(38000)
    pwm5.duty(1000)
    pwm6=machine.PWM(p6)
    pwm6.freq(38000)
    pwm6.duty(0)
    pwm7=machine.PWM(p7)
    pwm7.freq(38000)
    pwm7.duty(100)
    pwm8=machine.PWM(p8)
    pwm8.freq(38000)
    pwm8.duty(0)




def turnleft:
    pwm1=machine.PWM(p1)
    pwm1.freq(38000)
    pwm1.duty(100)
    pwm2=machine.PWM(p2)
    pwm2.freq(38000)
    pwm2.duty(0)
    pwm3=machine.PWM(p3)
    pwm3.freq(38000)
    pwm3.duty(1000)
    pwm4=machine.PWM(p4)
    pwm4.freq(38000)
    pwm4.duty(0)
    pwm5=machine.PWM(p5)
    pwm5.freq(38000)
    pwm5.duty(100)
    pwm6=machine.PWM(p6)
    pwm6.freq(38000)
    pwm6.duty(0)
    pwm7=machine.PWM(p7)
    pwm7.freq(38000)
    pwm7.duty(1000)
    pwm8=machine.PWM(p8)
    pwm8.freq(38000)
    pwm8.duty(0)


def stop:
    pwm1=machine.PWM(p1)
    pwm1.freq(38000)
    pwm1.duty(0)
    pwm2=machine.PWM(p2)
    pwm2.freq(38000)
    pwm2.duty(0)
    pwm3=machine.PWM(p3)
    pwm3.freq(38000)
    pwm3.duty(0)
    pwm4=machine.PWM(p4)
    pwm4.freq(38000)
    pwm4.duty(0)
    pwm5=machine.PWM(p5)
    pwm5.freq(38000)
    pwm5.duty(0)
    pwm6=machine.PWM(p6)
    pwm6.freq(38000)
    pwm6.duty(0)
    pwm7=machine.PWM(p7)
    pwm7.freq(38000)
    pwm7.duty(0)
    pwm8=machine.PWM(p8)
    pwm8.freq(38000)
    pwm8.duty(0)

while(True):
    lcd.display(sensor.snapshot())
