import json
import time
import eventlet
from SocketService import SocketService
import logging
import socketio

logging.basicConfig(level=logging.INFO)


class SocketIO(SocketService):
    def __init__(self):
        super().__init__()
        self.app = None
        self.sio = socketio.Server()
        self.payload = None
        self.connections = {}

    def find_connection_by_user_id(self, user_id):
        logging.info("SocketIO: Updating payload")
        user_sid = self.connections[user_id]
        self.notify(self.payload, user_sid)

    def notify(self, sid, user_sid):
        logging.info("SocketIO: Notifying clients")
        print(f"## Sent to: {user_sid}")
        self.sio.emit('notify', json.dumps(self.payload), room=user_sid)

    def run(self, host='localhost', port=5000):
        @self.sio.event
        def receive_report(sid, data):
            self.payload = json.loads(data)
            self.find_connection_by_user_id(self.payload["user_id"])

        @self.sio.event
        def user_connected(sid, data):
            self.connections[data["user_id"]] = sid
            print(self.connections)

        @self.sio.event
        def connect(sid, environ):
            print(f"Client {sid} connected to /notifications")

        @self.sio.event
        def disconnect(sid):
            print(f"Client {sid} disconnected from /notifications")

        # Use eventlet to run the Socket.IO server
        app = socketio.WSGIApp(self.sio)
        eventlet.wsgi.server(eventlet.listen((host, 5000)), app)

        # Event handler for "/receive_report"


if __name__ == "__main__":
    socket_server = SocketIO()
    socket_server.run()

    try:
        while True:
            # Simulate some ongoing process
            time.sleep(1)
    except KeyboardInterrupt:
        # Gracefully handle KeyboardInterrupt to disconnect clients
        pass
    finally:
        socket_server.sio.disconnect()
