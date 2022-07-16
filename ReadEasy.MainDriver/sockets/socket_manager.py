import socketio
from sockets.main_namespace import MainNamespace
from sockets.mistakes_namespace import MistakesNamespace

class SocketManager():
    def __init__(self) -> None:
        self.sio = socketio.Client()
        self.sio.register_namespace(MainNamespace('/main'))
        self.sio.register_namespace(MistakesNamespace('/mistakes'))

    def init_main_socket(self):
        self.sio.connect('http://localhost:4000', namespaces=['/main'])

    def init_mistakes_socket(self):
        self.sio.connect('http://localhost:4000', '/mistakes')