# client

import socket
getHOST = (raw_input('Enter The Host: '))

HOST = getHOST
getPORT = (input('Enter Port: '))

PORT = getPORT        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

NICK = 'ARDI' #raw_input('Welcome, Enter your name: ')

while True:
    MSG = raw_input('>> ')
    if MSG == "exit" :
        print "Disconnect..."
        break
    else :
        MSG = NICK + ': ' + MSG
    s.send(MSG)
    
    data = s.recv(1024)
    if not data :
        print "Disconnect..."
        break
    else :
        print data
    
s.close()

