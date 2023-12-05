# tcp_server.py

import socket

HOST = "127.0.0.1"                                                              # the server's hostname or IP address
PORT = 65432                                                                    # the port used by the server

# the server runs at localhost
# server receives data and echoes it back to the client

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)