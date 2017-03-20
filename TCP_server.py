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

server.listen(1)
print "[*] Started listening on", ip, ":", port

while True:

	client, addr_cl = server.accept()
	print "[*] Got a connection from ", addr_cl[0], ":", addr_cl[1]

	data = client.recv(1024)
	if not data:
		print "[*] Disconnected from ", addr_cl[0], ":", addr_cl[1]
		client.close()
		continue
	data_split = data.split(" ")

	print "[*] Received \'", data, "\' from the client."
	print "    Processing data: "

	if len(data_split) != 3:
		client.send("300 -1 Incorrect format. Try again. \"OC 1 2\"")
		print "    Processing done. Invalid data.\n[*] Reply sent"
		print "[*] Disconnected from ", addr_cl[0], ":", addr_cl[1]
		client.close()
		continue

	if not (isInteger(data_split[1]) and isInteger(data_split[2])):
		client.send("300 -1 Noninteger operands. Try again. \"OC 1 2\"")
		print "    Processing done. Invalid data.\n[*] Reply sent"
	else:
		if(data_split[0] == "+"):
			client.send('200 ' + str(int(data_split[1]) + int(data_split[2])))
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "-"):
			client.send('200 ' + str(int(data_split[1]) - int(data_split[2])))
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "*"):
			client.send('200 ' + str(int(data_split[1]) * int(data_split[2])))
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "/"):
			if int(data_split[2]) == 0:
				client.send("300 -1 Attempted division by zero. Try again. \"OC 1 2\"")
				print "    Processing done. Invalid data.\n[*] Reply sent"
				continue
			client.send('200 ' + str(int(data_split[1]) / int(data_split[2])))
			print "    Processing done.\n[*] Reply sent"

		else:
			client.send("300 -1 Invalid operator. Try again. \"OC 1 2\"")
			print "    Processing done. Invalid data.\n[*] Reply sent"

	print "[*] Disconnected from ", addr_cl[0], ":", addr_cl[1]

	client.close()

server.close()