import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()

print("server running...\n")

client_socket, client_address = server.accept()
client_socket.send("your server connection is made.\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print("exit made...")
        break
    else:
        print(f"{message}\n")
        message = input("message: ")
        client_socket.send(message.encode(FORMAT))

server.close()