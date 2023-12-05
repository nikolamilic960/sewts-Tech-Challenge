# tcp_client.py

import socket
import random
import time

HOST = "127.0.0.1"                                                              # the server's hostname or IP address
PORT = 65432                                                                    # the port used by the server

start_time = time.perf_counter()
last_send_time = time.perf_counter()
cnt = 0                                                                         # counter for data sending


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while (time.perf_counter() - start_time <= 5.0):
        if (time.perf_counter() - last_send_time >= 0.100):                     # data is sent when 100ms has passed from the last time data was sent
            cnt += 1
            last_send_time = time.perf_counter()
            print(last_send_time - start_time)

            num = random.randint(0, 2**32 -1)                                   # random integer number
            print('Generated number: ' + str(num))
            if (cnt % 5 == 0):                                                    #bit-0 toggling every 500ms
                temp = num ^ (1 << 31)
                print('Generated number after bit-0 toggling: ' + str(temp))
            num_bin = (format(num, 'b')).zfill(32)                              # integer number converted to 32-bit binary string

            s.sendall(bytes(num_bin, 'utf-8'))
            data = s.recv(1024)
            print(f"Received {data!r}")