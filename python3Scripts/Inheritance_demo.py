class Process(object):
    def __init__(self):
        print('init Process')

    def process_function(self):
        return "process_function"

class Client(Process):
    def __init__ (self):
        print('init Client')

    def process_function(self):
        return "client_function"

class Server(Process):
    def __init__(self):
        print('init Server')

    def process_function(self):
        result = super(Server,self).process_function()
        return result + ", server_function"

class BackgroundProcess(Process):
    pass

p = Process()
c = Client()
s = Server()
b = BackgroundProcess()

processes = [p, c, s, b]

print()
for m in processes:
    print(m.process_function())
