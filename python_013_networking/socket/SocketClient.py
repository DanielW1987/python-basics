import socket

client_socket = socket.socket()

client_socket.connect(("localhost", 4000))
message = client_socket.recv(1024)

while message:
    print("Received:", message.decode())
    message = client_socket.recv(1024)

client_socket.close()
