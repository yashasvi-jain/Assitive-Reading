import socketio

if __name__ == '__main__':
    sio = socketio.Client()
    try:
        sio.connect('http://localhost:4000')
        @sio.on('*')
        def catch_all(event, data):
            print('something')
            print(event)
            print(data)

        print('my session id:', sio.sid)
    except:
        pass