import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
while True:
    message = raw_input("Enter the message: ")
    print "response from server", c.hello(message)
