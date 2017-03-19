import socket
import random

addr = ( socket.gethostbyname(socket.gethostname()), 50010 )
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(addr)

print "[*] Server open on", addr[0], ":", addr[1]

while True:
	data_rc, addr_cl = server.recvfrom(1024)
	if random.randrange(10) > 4:
		continue
	print "received message \"", data_rc, "\" from ", addr_cl[0], " : ", addr_cl[1]
	if data_rc == "Exit" or data_rc == "exit":
		break

server.close()