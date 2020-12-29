#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
m=0
while m<10:
   c.send(b'Thank you for connecting')
   time.sleep(3)
   m += 1