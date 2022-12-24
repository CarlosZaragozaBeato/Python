import socket

HOST = '192.168.1.141'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("HELLO WORLD".encode('utf-8'))
print(socket.recv(1024))
