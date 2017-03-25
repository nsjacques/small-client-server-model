import socket

#gets query from user
message = raw_input("Enter an operator and two numbers, in that order delimited by spaces (\'exit\' to quit): ")
#sets up address
address = ( socket.gethostbyname(socket.gethostname()), 50010 )

if message.lower() != "exit":

	#makes socket for the address
	client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	#sends input message
	client.sendto(message, address)

	#handles dropped packets
	delay = 0.1
	while delay < 2:
		client.settimeout(delay)
		try:
			response = client.recv(1024).split(" ")
			break
		except socket.timeout:
			delay*=2


	# if the packet was recieved
	# responses
		# I'm only leaving the "else" there in case you create some unhandled issue
		# that i have not seen and want to have some idea where you are.
		# I believe responses are partitioned by the first two
	if delay < 2:
		if response[0] == "200":
			print "Status Code: ", response[0], "\nResponse: ", response[1]

		elif response[0] == "300":
			print "Status Code: ", response[0], "\nResponse: ", response[1], "\nMessage: ", " ".join(response[2:])
		else:
			print "This should never happen"
			print "rep[0]", response[0], " rep[1]", response[1]

	# if the packet got dropped
	else:
		print "Timeout"

	client.close()