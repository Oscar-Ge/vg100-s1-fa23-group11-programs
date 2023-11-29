import machine
from fpioa_manager import fm
from Maix import GPIO
import time

# 定义引脚映射
step_pin = 11  # pin11
dir_pin = 10   # pin12

# 初始化引脚
fm.register(step_pin, fm.fpioa.GPIOHS0, force=True)
fm.register(dir_pin, fm.fpioa.GPIOHS1, force=True)

step_motor = GPIO(GPIO.GPIOHS0, GPIO.OUT)
dir_motor = GPIO(GPIO.GPIOHS1, GPIO.OUT)

# 设置步进电机的步数和方向
def set_motor_steps(direction, steps):
    dir_motor.value(direction)
    for i in range(steps):
        step_motor.value(1)
        time.sleep_ms(1)  # 控制步进电机步进脉冲的时间间隔
        step_motor.value(0)
        time.sleep_ms(1)

# 控制步进电机顺时针旋转
set_motor_steps(1, 200)

# 停顿一段时间
time.sleep(1)

# 控制步进电机逆时针旋转
set_motor_steps(0, 200)
