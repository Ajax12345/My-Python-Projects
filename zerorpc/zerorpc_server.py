import zerorpc

class HelloRPC(object):
    def hello(self, name):
        #return "message from host: %s" % name
        print "message from host: %s" % name

        return raw_input("Enter your message: ") 

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
