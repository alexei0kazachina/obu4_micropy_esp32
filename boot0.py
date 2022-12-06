# This file is executed on every boot (including wake-boot from deepsleep)
import esp32
#esp.osdebug(None)
import webrepl
webrepl.start()
try:
  import usocket as socket
except:
   import socket

import network
from machine import Timer
import time

import esp 
#esp.osdebug(None) 
import gc 
gc.collect() 
ssid = 'CMControl' 
password = 'K0jzgsf=!' 
ap = network.WLAN(network.STA_IF) 
ap.active(True) 
ap.connect(ssid, password) 
while ap.isconnected() == False: 
   print('.')
   time.sleep(5)
print('Connection successful') 
print(ap.ifconfig())
