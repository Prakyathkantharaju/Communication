# general purpose import
import socket, logging
import time

class UDP():
    def __init__(self, ip = 'localhost', port = 5005):
        # setup the communication
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.port = port
        self.ip = ip
        
    def send(self, i):
        # send the message by encode the string to bytes
        data = str(i)
        MESSAGE = bytes(data, "UTF-8")
        # MESSAGE = str(i).encode('utf-8')
        print(MESSAGE, type(MESSAGE))
        self.sock.sendto(MESSAGE, (self.ip,self.port ))

    def close(self):
        logging.warning('closing the socket')
        self.sock.close()

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    MESSAGE = bytes("0", "UTF-8")
    sock.sendto(MESSAGE, ('localhost', 5005))
    an = UDP()
    i = 1
    while i < 10000:
        i += 1
        an.send(i)
        time.sleep(1)
        print(i)
    an.close()