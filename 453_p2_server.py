import socket

#create TCP socket object
#bind it to an address
#receive an incoming connection from a client
#recieve data from client
#send data to client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "10.0.0.15"
port = 50001
address = (ip, port)

server.bind(address)
server.listen(2)
print "[*] Started listening on", ip, ":", port

client, addr_cl = server.accept()
print "[*] Got a connection from ", addr_cl[0], ":", addr_cl[1]

while True:
	data = client.recv(1024)
	print "[*] Recieved ", data, " from the client"
	print "    Processing data"

	if(data == "Hello server"):
		client.send("Hello client")
		print "    Processing done.\n[*] Reply sent"
	elif(data == "disconnect"):
		client.send("Goodbye")
		client.close()
		break
	else:
		client.send("Invalid data")
		print "    Processing done. Invalid data.\n[*] Reply sent"

server.close()





#fun: >>> import socket
#>>> name = socket.gethostname()
#>>> print name
#Noahs-MacBook-Pro-3.local
#>>> socket.gethostbyname(name)
#'10.0.0.15'