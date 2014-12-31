from http.server import *
import userManager
import socket
import struct
import os
from threading import Thread

HOST = ''
PORT = 80

import socket, struct

def get_default_gateway_linux():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def get_ip():
    file=os.popen("ipconfig")
    data=file.read()
    file.close()
    for line in data.strip().split('\n'):
        if "IPv4 Address" in line:
            return line
    return "Could not find address"
try:
    print(get_default_gateway_linux())
except:
    print(get_ip())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

def conCurr():
    userManager.UserManager(conn,addr)
    
while(True):
    s.listen(1)
    conn, addr = s.accept()
    print("Got connection; " + str(addr))
    Thread(target = conCurr).start()
    
