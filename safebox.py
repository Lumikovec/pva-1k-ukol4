import socket
import time

s = socket.create_connection(("167.114.184.11", 9100), timeout=5)

print(s.recv(4096).decode())

code = (int(time.time()) * 7919) % 100000
s.sendall(f"{code}:Filip Smetana\n".encode())

print(repr(s.recv(4096)))

s.close()
