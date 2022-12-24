import socket

HOST = '192.168.1.141'#socket.gethostbyname(socket.gethostname())
PORT = 9090
#HOST = '192.168.1.141'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is {message}")
    communication_socket.send(f"Got you message".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended")