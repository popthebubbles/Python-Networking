#sends data to a server and gets a reply

import socket #for sockets
import sys #for exit

#creates an AF_INET, STREAM socket (TCP)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create a new socket. Error code:', str(msg[0]), 'Error Message:', str(msg[1])
    sys.exit()

print 'Socket Created.'

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve host name
    print 'Host name could not be resolved.'
    sys.exit()

print 'IP address of', host, 'is', remote_ip

s.connect((remote_ip, port))

print 'Socket connected to', host, 'on ip', remote_ip

message = "GET / HTTP/1.1\r\n\r\n"

try:
    #sends the whole string
    s.sendall(message)
except socket.error:
    print 'Send Failed'
    sys.exit()

print('Message send successful')

reply = s.recv(4096)

print reply

s.close()