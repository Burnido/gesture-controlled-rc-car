from machine import I2C, Pin, UART
import time
from mpu6050 import MPU6050

# I2C: SCL=GP0, SDA=GP1
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
print(i2c.scan())
mpu = MPU6050(i2c)

# UART1: TX=GP4, RX=GP5 (to HC-05)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
# For Pico's USB Serial output to your PC
import sys

def get_command(ax, ay):
    if ay > 0.5:
        return 'F'  # Forward
    elif ay < -0.5:
        return 'B'  # Backward
    elif ax > 0.5:
        return 'R'  # Right
    elif ax < -0.5:
        return 'L'  # Left
    else:
        return 'S'  # Stop

while True:
    accel = mpu.get_accel_data()
    ax = accel['x']
    ay = accel['y']

    cmd = get_command(ax, ay)
    uart.write(cmd)

    # Show on Thonny or Pico serial console
    print(f"Accel X: {ax:.2f}, Y: {ay:.2f} → Sending: {cmd}")

    time.sleep(0.2)
