import socketio
from sockets.main_namespace import MainNamespace
from sockets.mistakes_namespace import MistakesNamespace

class SocketManager():
    def __init__(self) -> None:
        self._sio = socketio.Client()
        self._sio.register_namespace(MainNamespace('/main'))
        self._sio.register_namespace(MistakesNamespace('/mistakes'))

    def init_main_socket(self):
        self._sio.connect('http://localhost:4000', '/main')

    def init_mistakes_socket(self):
        self._sio.connect('http://localhost:4000', '/mistakes')