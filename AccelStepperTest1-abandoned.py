import machine
import utime

class StepperMotor:
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pins = [machine.Pin(pin1, machine.Pin.OUT),
                     machine.Pin(pin2, machine.Pin.OUT),
                     machine.Pin(pin3, machine.Pin.OUT),
                     machine.Pin(pin4, machine.Pin.OUT)]
        self.sequence = [[1, 0, 0, 1],
                         [1, 0, 0, 0],
                         [1, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 1, 0],
                         [0, 0, 1, 0],
                         [0, 0, 1, 1],
                         [0, 0, 0, 1]]
        self.step_delay = 0.005  # 调整步进间隔

    def step_forward(self, steps):
        for _ in range(steps):
            for step in self.sequence:
                self._set_pins(step)
                utime.sleep(self.step_delay)

    def step_backward(self, steps):
        for _ in range(steps):
            for step in reversed(self.sequence):
                self._set_pins(step)
                utime.sleep(self.step_delay)

    def _set_pins(self, values):
        for pin, value in zip(self.pins, values):
            pin.value(value)

# 设置步进电机引脚
motor = StepperMotor(6, 5, 4, 3)

# 步进电机正转10步
motor.step_forward(10)

# 等待一段时间
utime.sleep(1)

# 步进电机反转10步
motor.step_backward(10)
