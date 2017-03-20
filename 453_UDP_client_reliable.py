import socket

message = raw_input("Enter an operator and two numbers, in that order delimited by spaces (\'exit\' to quit): ")
address = ( socket.gethostbyname(socket.gethostname()), 50010 )

if message.lower() != "exit":

	client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	client.sendto(message, address)

	response = client.recv(1024).split(" ")

	if response[0] == "200":
		print "Status Code: ", response[0], "\nResponse: ", response[1]

	elif response[0] == "300":
		print "Status Code: ", response[0], "\nResponse: ", response[1], "\nMessage: ", " ".join(response[2:])
	else:
		print "This should never happen"
		print "rep[0]", response[0], " rep[1]", response[1]

	client.close()