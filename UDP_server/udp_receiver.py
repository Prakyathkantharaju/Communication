# This setup of socket object is same as the regular UDP
import socket
import sys

HOST, PORT = "localhost", 9999
data =  test
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 51005))
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")
# printing out the data
print(f'Sent:     {data}')
print(f'Received: {recevied}')'