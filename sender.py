import socket
import os

sending_file = 'sending_file.txt'

if not os.path.exists(sending_file):
    with open(sending_file, 'w') as f:
        f.write("Dies ist eine automatisch erstellte Test-Datei.")
    print(f"Datei {sending_file} wurde neu erstellt.")

server_ip = '10.25.140.8'
port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

with open(sending_file, 'rb') as f:
    data = f.read(1024)
    while data:
        client_socket.sendall(data)
        data = f.read(1024)

client_socket.close()