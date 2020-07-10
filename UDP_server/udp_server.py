import socketserver
import threading, time

class data(object):
    def __init__(self):
        self.my_data = 1




class UDPrequest(socketserver.BaseRequestHandler, data):
    # def data(self):
    #     return self.my_data

    def handle(self):
        data = self.request[0].strip()
        data = data.decode()
        socket = self.request[1]
        print('{} wrote'.format(self.client_address[0]))
        print(self.my_data.my_data)
        socket.sendto(str(self.my_data.my_data).encode('utf-8'), self.client_address)
    
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # This is for server forever
    # with socketserver.UDPServer((HOST, PORT), UDPrequest) as server:
        # server.serve_forever()
    # threading option
    server = ThreadedUDPServer((HOST, PORT), UDPrequest)
    test = server.RequestHandlerClass
    # test.setup()
    test.my_data = data()
    # print(test.data())
    with server:
        ip,port = server.server_address
        server_thread = threading.Thread(target= server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread")
        i = 1
        while i < 1000:
            i += 1
            time.sleep(1)
            threading.Lock()
            # server.my_data = i
            print(test.my_data.my_data)
            test.my_data.my_data = i
            print('in the loop')
        server.shutdown()