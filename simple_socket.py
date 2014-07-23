#implements error handling

import socket #for sockets
import sys #for exit

#creates an AF_INET, STREAM socket (TCP)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create a new socket. Error code:', str(msg[0]), 'Error Message:', str(msg[1])
    sys.exit()

print('Socket Created.')
