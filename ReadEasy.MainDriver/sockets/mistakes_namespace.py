import socketio
sio = socketio.Client()

class MistakesNamespace(socketio.ClientNamespace):
    def on_connect(self):
        print('Connected to Reading Socket!')

    def on_disconnect(self):
        print('Disconnected from Reading Socket!')

sio.register_namespace(MistakesNamespace('/mistakes'))