import socketio
import eventlet
import time

# Create a Socket.IO client instance
sio = socketio.Client()

# Connect to the Socket.IO server



# Event handler for successful connection
@sio.event
def connect():
    print("Connected to server")
    sio.emit('user_connected', {"user_id": "1234"}, namespace='/')

@sio.event
def notify(data):
    print(f"Received data: {data}")

# Event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from server")


# Method to send data to "/receive_report"


# Example: Sending a report every 5 seconds
if __name__ == "__main__":
    try:
        sio.connect('http://127.0.0.1:5000')
        sio.wait()
    except KeyboardInterrupt:
        sio.disconnect()
