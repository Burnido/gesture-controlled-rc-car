# mpu6050.py
from machine import I2C
import time

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        # Wake up the MPU6050 as it starts in sleep mode
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')  

    def read_raw_data(self, reg):
        # Read two bytes of data starting from reg
        high = self.i2c.readfrom_mem(self.addr, reg, 1)
        low = self.i2c.readfrom_mem(self.addr, reg + 1, 1)
        value = (high[0] << 8) | low[0]
        if value > 32767:
            value -= 65536
        return value

    def get_accel_data(self):
        # Read accelerometer raw values
        ax = self.read_raw_data(0x3B) / 16384.0
        ay = self.read_raw_data(0x3D) / 16384.0
        az = self.read_raw_data(0x3F) / 16384.0
        return {'x': ax, 'y': ay, 'z': az}

    def get_gyro_data(self):
        # Read gyroscope raw values
        gx = self.read_raw_data(0x43) / 131.0
        gy = self.read_raw_data(0x45) / 131.0
        gz = self.read_raw_data(0x47) / 131.0
        return {'x': gx, 'y': gy, 'z': gz}
