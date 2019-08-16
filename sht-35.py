# coding: utf-8


import smbus
import time


addr = 0x45
i2c = smbus.SMBus(1)


def calculation(t_data, h_data):
    Humidity = 100.0 * float(h_data) / 65535.0
    Temperature = -45.0 + 175.0 * float(t_data) / 65535.0
    return Humidity, Temperature


while True:
    i2c.write_i2c_block_data(addr, 0x2C, [0x06])
    time.sleep(0.05)
    data = i2c.read_i2c_block_data(addr, 0x00, 12)
    time.sleep(0.05)

    # Devide data into counts Temperature
    t_data = data[0] << 8 | data[1]
    # Devide data into counts Humidity
    h_data = data[3] << 8 | data[4]

    print(calculation(t_data, h_data))
