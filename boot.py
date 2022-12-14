# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import machine

import bme280

import network

try:
  import usocket as socket
except:
  import socket

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'holod'
password = '77700609'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())