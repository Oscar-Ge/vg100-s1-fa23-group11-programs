import machine
from fpioa_manager import fm
from Maix import GPIO
import time

# 定义引脚映射
step_pin1 = 11  # pin11
dir_pin1 = 10   # pin12
step_pin2 = 21  # pin2
dir_pin2 = 22   # pin3

# 初始化引脚
fm.register(step_pin1, fm.fpioa.GPIOHS0, force=True)
fm.register(dir_pin1, fm.fpioa.GPIOHS1, force=True)
fm.register(step_pin2, fm.fpioa.GPIOHS2, force=True)
fm.register(dir_pin2, fm.fpioa.GPIOHS3, force=True)

step_motor1 = GPIO(GPIO.GPIOHS0, GPIO.OUT)
dir_motor1 = GPIO(GPIO.GPIOHS1, GPIO.OUT)
step_motor2 = GPIO(GPIO.GPIOHS2, GPIO.OUT)
dir_motor2 = GPIO(GPIO.GPIOHS3, GPIO.OUT)

# 设置步进电机的步数和方向
def set_motor1_steps(direction, steps):
    dir_motor1.value(direction)
    for i in range(steps):
        step_motor1.value(1)
        time.sleep_ms(1)  # 控制步进电机步进脉冲的时间间隔
        step_motor1.value(0)
        time.sleep_ms(1)
def set_motor2_steps(direction, steps):
    dir_motor2.value(direction)
    for i in range(steps):
        step_motor2.value(1)
        time.sleep_ms(1)  # 控制步进电机步进脉冲的时间间隔
        step_motor2.value(0)
        time.sleep_ms(1)
while True:
    # 控制步进电机顺时针旋转
    set_motor1_steps(1, 200)
    set_motor2_steps(1, 500)
    # 停顿一段时间
    time.sleep(1)
    # 控制步进电机逆时针旋转
    set_motor1_steps(0, 200)
    set_motor2_steps(0, 500)
    time.sleep(1)
