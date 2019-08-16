# coding: utf-8
# http://www.mouser.com/ds/2/682/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital-971521.pdf

import smbus
import time


class SHT35:
    def __init__(self):

        self.addr = 0x45
        self.cmd_msb = 0x2C
        self.cmd_lsb = 0x06 # high repeatability
        self.i2c = smbus.SMBus(1)
        self.buffer_size = 12

    def read(self):

        self.i2c.write_i2c_block_data(self.addr, self.cmd_msb, [self.cmd_lsb])
        time.sleep(0.05)
        data = self.i2c.read_i2c_block_data(self.addr, 0x00, self.buffer_size)
        time.sleep(0.05)

        # Devide data into counts Temperature
        t_data = data[0] << 8 | data[1]
        # Devide data into counts Humidity
        h_data = data[3] << 8 | data[4]
        return calculation(t_data, h_data)

    @staticmethod
    def calculation(t_data, h_data):
        Humidity = 100.0 * float(h_data) / 65535.0
        Temperature = -45.0 + 175.0 * float(t_data) / 65535.0
        return Humidity, Temperature

if __name__ =="__main__":
    sht35=SHT35()
    print(sht35.read())
