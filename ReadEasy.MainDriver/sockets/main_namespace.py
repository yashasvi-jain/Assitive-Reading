import socketio
from main import Main

class MainNamespace(socketio.ClientNamespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)

    def on_connect(self):
        print('Connected to Main namespace')

    def on_disconnect(self):
        print('Disconnected from Main namespace')

    def on_read(self, data):
        print('Read event')
        main = Main()
        main.main(self, data)

    def on_transfer(sid, data):
      return data