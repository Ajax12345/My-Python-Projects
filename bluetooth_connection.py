#server and client for bluetooth


#client:

import socket

address = ""

port = 3

s = socket.socket.(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

s.connect((address, port))
while True:
    data = "" #substitute with Pickled? commands for helicopter
    s.send(bytes(data, 'UTF-8')) #will probably need to change this


s.close()


#server:

address = ""
port = 3
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK__STREAM, socket.BTPROTO_RFCOMM)

s.bind((address, port))
s.listen(backlog)
try:
    client, address = s.accept()
    while True:
        data = client.recv(size)
        if data:
            print data

            client.send(data) #will have to change this to send pickled? data

except:
    print "unable to work"
    client.close()
    s.close()
