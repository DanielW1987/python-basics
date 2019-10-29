import socket

host: str = "localhost"
port: int = 5000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IP4

my_socket.bind((host, port))
my_socket.listen(1)
print("Server is listening on port:", str(port))
connection, address = my_socket.accept()

file_name: str = connection.recv(1024).decode()

try:
    file = open(file_name, "rb")
    content = file.read()
    connection.send(content)
    file.close()
except FileNotFoundError:
    print("File does not exist")
    connection.send("File does not exist".encode())

connection.close()
