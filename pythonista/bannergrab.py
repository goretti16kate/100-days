#!/usr/bin/env python3
import socket

s = socket.socket()

s.connect(("45.33.32.156",22))
answer = s.recv(1024)

print (answer)
s.close