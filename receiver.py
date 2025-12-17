import socket
print('test')
host = '0.0.0.0'
port = 6769
file_name = "temporary.txt"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

conn, addr = server_socket.accept()

with open(file_name, "wb") as f:
    while True:
        data = conn.recv(1024) # Empfange Daten in 1KB Häppchen
        if not data:
            break
        f.write(data)

print("received data")
conn.close()
server_socket.close()