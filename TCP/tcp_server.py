# general imports
import socket, sys, logging

class TCP():
    def __init__(self, local_ip = 'localhost', local_port = '5005', 
                    remote_ip = 'localhost',remote_port = '9999'):
        # setup the communication
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # TCP
        self.local_port = local_port
        self.local_ip = local_ip
        # Temp variable
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        
    def _setup(self):
        self.sock.bind((self.local_ip,self.local_port))
        self.sock.listen()

    def send_remote(self, i):
        # This if you know the address of the server.
        MESSAGE = str(i).encode('utf-8')
        self.sock.sendto(MESSAGE, (self._ip,self.port ))

    def close(self):
        logging.warning('closing the socket')
        self.sock.close()



