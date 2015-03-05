#!/usr/bin/env python



import socket
import sys
# 
#  
# 
# 
# port = 70
# host = sys.argv[1]
# filename = sys.argv[2]
# 
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 
# try:
#     s.connect((host,port))
# except socket.gaierror, e:
#     print "Error connecting to server: %s" % e
#     sys.exit(1)
# 
# s.sendall(filename + "\r\n")
# 
# 
# while True:
#     buf = s.recv(2048)
#     if not len(buf):
#         break
#     sys.stdout.write(buf)


host = ''
port = 10080

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,e:
    print "Strange error creating socket: %s" % e
    sys.exit()
    
    
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

print "server is running"

while True:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("Welcome," + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.write("Love you,sir")
    clientfile.close()
    clientsock.close()



