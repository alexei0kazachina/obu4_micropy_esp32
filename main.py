i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
bme = bme280.BME280(i2c=i2c)
print(bme.values)

from machine import Pin
led = Pin(5, Pin.OUT)
def web_page(): 
   if led.value() == 1: 
      gpio_state="ВКЛ"
   else: 
      gpio_state="ВЫКЛ"
   html = """
   <!DOCTYPE html>
   <head>
   <meta charset="utf-8">
   <title>Состояние реле компрессор</title
   <link rel="stylesheet" href="stile.css">
   <style>
   .button {
   border: none;
   color: white;
   padding: 15px 32px;
   text-align: center;
   text-decoration: none;
   display: inline-block;
   font-size: 16px;
   margin: 4px 2px;
   cursor: pointer;
   }

   .button1 {background-color: #4CAF50;} /* Green */
   .button2 {background-color: #008CBA;} /* Blue */
   </style>
   </head>
   <body>
   <div align="center">
   <h1>Состояние реле K1</h1>
   <p>GPIO state:<strong>""" + gpio_state + """</strong></p>
   <p><a href="/?led=on"><button class="button button1">ВКЛ</button></a></p>
   <p><a href="/?led=off"><button class="button button2">ВЫКЛ</button></a></p>
   </div> 
  </body>
   
   </html>"""
   return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)
while True:
  conn, addr = s.accept()
  print('Got a connection from %s'%str(addr))
  request = conn.recv(1024)
  request =str(request)
  print('Content = %s'% request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on ==6:
    print('LED ON')
    led.value(1)
  if led_off ==6:
    print('LED OFF')
    led.value(0)
  response =web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
