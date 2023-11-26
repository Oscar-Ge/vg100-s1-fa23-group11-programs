import sensor, image, lcd, time
import KPU as kpu
import gc, sys
from fpioa_manager import fm
import machine
import AccelStepper

stepper1=AccelStepper()
stepper1._pin=[6, 5, 4, 3]
stepper2=AccelStepper()
stepper2._pin=[10, 9, 8, 7]

# 设置步进电机的最大速度和加速度
stepper1.set_max_speed(200)  # 根据电机规格设置合适的最大速度（步/秒）
stepper1.set_acceleration(100)  # 根据电机规格设置合适的加速度（步/秒^2）
stepper2.set_max_speed(200)  # 根据电机规格设置合适的最大速度（步/秒）
stepper2.set_acceleration(100)  # 根据电机规格设置合适的加速度（步/秒^2）

def stepper(target_position):
    motor.move_to(target_position)
    while motor.is_running():
        motor.run_speed()
    motor.stop()
    print("I have passed the step:", target_position)

stepper(input())

