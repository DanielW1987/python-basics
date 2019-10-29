import socket

client_socket = socket.socket()

client_socket.connect(("localhost", 5000))

file_name: str = input("Enter a file name: ")

client_socket.send(file_name.encode())
content = client_socket.recv(1024)
print(content.decode())

client_socket.close()
