# server
import socket
import thread

HOST = '127.0.0.1'               # Symbolic name meaning the local host
PORT = 2022                     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
   
while True:
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data :
            print "Disconnect...", addr
            break
        
        elif data[6:] == "list" :
            data = open ('./list.txt').read()
            conn.send(data)
            
        elif data[6:] == "1" :
            data = open ('./A.txt').read()
            conn.send(data)
            print addr, "Opening file A.txt"

        elif data[6:] == "2" :
            data = open ('./b.xml').read()
            conn.send(data)
            print addr, "Opening file b.xml"
        
        else :
            conn.send(data)
            print data
conn.close()
