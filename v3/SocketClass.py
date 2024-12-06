import socket            

class Ssocket:
    def __init__(self, side):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.c = ""      
        self.port = 8866
        self.connect_ip = "localhost"
        self.side = side

    def bind_socket(self):
        self.s.bind((self.connect_ip, self.port))        
        print ("socket binded to %s" %(self.port))
    
    def listen_port(self,time):
        self.s.listen(time)    
        print ("socket is listening")
        c, addr = self.s.accept()    
        print ('Got connection from', addr)
        self.c = c

    def client_connect(self):
        self.s.connect((self.connect_ip, self.port))
        print("The connection is established")

    def send_data(self, data):
        if self.side == "s":
            self.c.send(data.encode())
        elif self.side == "c":
            self.s.send(data.encode())

    def receive_data(self):
        if self.side == "s":
            res = self.c.recv(1024).decode()
        elif self.side == "c":
            res = self.s.recv(1024).decode()
        return res