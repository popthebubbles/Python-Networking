import socket
import sys

HOST = ''
PORT = 8888 #Abitrary Port

#creates a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'

try:
    #binds to a port
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Failed to bind. Error Code: ' + str(msg[0]) + '. Error Message: ' + str(msg[1])
    sys.exit()

print 'Socket bind complete'

s.listen(10) #tells to listen and sets backlog
print 'Socket now listening'

while True:
    #wait to accept a connection- blocking call
    conn, addr = s.accept()

    #display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #respond
    data = conn.recv(1024)
    msg = 'Ok... ' + data
    
    if not data:
        break

    conn.sendall(msg)

conn.close()
s.close()