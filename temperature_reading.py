# geektechstuff
import time

from bmp280 import BMP280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus=SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

seconds_to_run = 100

for i in range(seconds_to_run):
    temperature = bmp280.get_temperature()
    print('The temperature is {:04.1f} degrees celesuis'.format(temperature))
    time.sleep(1)
