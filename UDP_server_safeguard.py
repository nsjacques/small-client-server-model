import socket
import random

#method used to test input validity
def isInteger(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

#creates socket and binds to address
addr = ( socket.gethostbyname(socket.gethostname()), 50010 )
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(addr)

print "[*] Server open on", addr[0], ":", addr[1]


while True:

	#recieves data
	data, addr_cl = server.recvfrom(1024)

	#drops packet 50% of the time
	if random.randrange(10) > 4:
		continue
	print "received message \"", data, "\" from ", addr_cl[0], " : ", addr_cl[1]


	
	# below handles and responds to data, valid and invalid:
	# this is exactly the same as TCP_server except it does not close a client socket


	if not data:
		server.sendto("300 -1 Incorrect format. Try again. \"OC 1 2\"", addr_cl)
		print "[*] Reply sent ", addr_cl[0], ":", addr_cl[1]
		continue

	data_split = data.split(" ")

	print "[*] Received \'", data, "\' from the client."
	print "    Processing data. "

	if len(data_split) != 3:
		server.sendto("300 -1 Incorrect format. Try again. \"OC 1 2\"", addr_cl)
		print "[*] Reply sent ", addr_cl[0], ":", addr_cl[1]
		continue

	if not (isInteger(data_split[1]) and isInteger(data_split[2])):
		server.sendto("300 -1 Noninteger operands. Try again. \"OC 1 2\"", addr_cl)
		print "    Processing done. Invalid data.\n[*] Reply sent"
	else:
		if(data_split[0] == "+"):
			server.sendto('200 ' + str(int(data_split[1]) + int(data_split[2])), addr_cl)
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "-"):
			server.sendto('200 ' + str(int(data_split[1]) - int(data_split[2])), addr_cl)
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "*"):
			server.sendto('200 ' + str(int(data_split[1]) * int(data_split[2])), addr_cl)
			print "    Processing done.\n[*] Reply sent"

		elif(data_split[0] == "/"):
			if int(data_split[2]) == 0:
				server.sendto("300 -1 Attempted division by zero. Try again. \"OC 1 2\"", addr_cl)
				print "    Processing done. Invalid data.\n[*] Reply sent"
				continue
			server.sendto('200 ' + str(int(data_split[1]) / int(data_split[2])), addr_cl)
			print "    Processing done.\n[*] Reply sent"

		else:
			server.sendto("300 -1 Invalid operator. Try again. \"OC 1 2\"", addr_cl)
			print "    Processing done. Invalid data.\n[*] Reply sent"

server.close()