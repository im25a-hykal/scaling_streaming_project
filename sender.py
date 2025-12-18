import socket
import keyboard
server_ip = '192.168.178.77'
port = 6769
sending_file = 'sending_file.txt'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

with open(sending_file, 'rb') as f:
    while True:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)
        if not data:
            break

client_socket.close()