from machine import Pin, I2C
from bmp180 import BMP180
from time import sleep as delay

i2c = I2C(scl=Pin(22), sda=Pin(21))
print('I2C scan:', i2c.scan())

bmp180 = BMP180(i2c)
bmp180.baseline = 10125

while True:
print('T: %.2fC P: %.1fPa A: %dm At: %dm' % (float(bmp180.temperature),
float(bmp180.pressure),
int(bmp180.altitude),((float(bmp180.pressure))/133)))
delay(5)
