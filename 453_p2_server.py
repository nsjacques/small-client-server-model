import socket

#create TCP socket object
#bind it to an address
#receive an incoming connection from a client
#recieve data from client
#send data to client

def isInteger(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

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
	if not data:
		continue
	data_del = data.split(" ")

	print "[*] Received \'", data, "\' from the client."
	print "    Processing data: "

	if not (isInteger(data_del[1]) and isInteger(data_del[2])):
		client.send("Noninteger operands. Try again. \"OC 1 2\"")
		print "    Processing interrupted. Invalid data.\n[*] Reply sent"
	else:
		if(data_del[0] == "+"):
			client.send(str(int(data_del[1]) + int(data_del[2])))
			print "    Processing done.\n[*] Reply sent"
			#client.close()
			#break
		elif(data_del[0] == "-"):
			client.send(str(int(data_del[1]) - int(data_del[2])))
			print "    Processing done.\n[*] Reply sent"
			#client.close()
			#break
		elif(data_del[0] == "*"):
			client.send(str(int(data_del[1]) * int(data_del[2])))
			print "    Processing done.\n[*] Reply sent"
			#client.close()
			#break
		elif(data_del[0] == "/"):
			if int(data_del[2]) == 0:
				client.send("Attempted division by zero. Try again. \"OC 1 2\"")
				print "    Processing interrupted. Invalid data.\n[*] Reply sent"
				continue
			client.send(str(int(data_del[1]) / int(data_del[2])))
			print "    Processing done.\n[*] Reply sent"
			#client.close()
			#break
		elif(data_del[0] == "X"):
			client.send("Goodbye")
			print "    Processing done.\n[*] Reply sent"
			client.close()
			break
		else:
			client.send("Invalid operator. Try again. \"OC 1 2\"")
			print "    Processing interrupted. Invalid data.\n[*] Reply sent"

server.close()





#fun: >>> import socket
#>>> name = socket.gethostname()
#>>> print name
#Noahs-MacBook-Pro-3.local
#>>> socket.gethostbyname(name)
#'10.0.0.15'