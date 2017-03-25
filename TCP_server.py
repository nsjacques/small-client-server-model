import socket

#method used to test input validity
def isInteger(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

def main():

	#creates socket and binds it to the address
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip = "10.0.0.15"
	port = 50003
	address = (ip, port)
	server.bind(address)

	#socket listens for at most one-at-a-time connections
	server.listen(1)
	print "[*] Started listening on", ip, ":", port

	#loops to allow multiple connections
	while True:

		#connects
		client, addr_cl = server.accept()
		print "[*] Got a connection from ", addr_cl[0], ":", addr_cl[1]

		#recieves data
		data = client.recv(1024)

		#begins validity checks:
		#empty string
		if not data:
			print "[*] Disconnected from ", addr_cl[0], ":", addr_cl[1]
			client.close()
			continue

		#splits for use
		data_split = data.split(" ")

		print "[*] Received \'", data, "\' from the client."
		print "    Processing data: "

		#invalid formatting
		if len(data_split) != 3:
			client.send("300 -1 Incorrect format. Try again. \"OC 1 2\"")
			print "    Processing done. Invalid data.\n[*] Reply sent"
			print "[*] Disconnected from ", addr_cl[0], ":", addr_cl[1]
			client.close()
			continue

		#invalid operands
		if not (isInteger(data_split[1]) and isInteger(data_split[2])):
			client.send("300 -1 Noninteger operands. Try again. \"OC 1 2\"")
			print "    Processing done. Invalid data.\n[*] Reply sent"
		#checks operator validity
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

if  __name__ == '__main__':
    main()