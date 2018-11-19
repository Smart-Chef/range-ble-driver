import socket

UDP_IP = "127.0.0.1"
# UDP_IP = "10.230.140.122"
UDP_PORT= 10000

MESSAGE = "Hello World"

# based on https://docs.python.org/2/howto/sockets.html

class MySocket:


    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

    
    def connect(self):
        self.sock.connect((UDP_IP, UDP_PORT))

    def mysend(self, message):
        self.sock.sendto(message, (UDP_IP, UDP_PORT))

    # def myread(self):
    #     self.sock.