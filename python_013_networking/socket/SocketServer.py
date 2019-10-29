import socket

host: str = "localhost"
port: int = 4000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IP4

my_socket.bind((host, port))
my_socket.listen(1)
print("Server is listening on port:", str(port))
connection, address = my_socket.accept()

print("Connection from: ", str(address))

connection.send("Hello from Server".encode())
connection.close()
