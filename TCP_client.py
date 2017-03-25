import socket

def main():

	#allows multiple connections in one session by looping

	while(True):

		#creates socket and creates address
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip=socket.gethostbyname(socket.gethostname())
		port = 50003
		address=(ip, port)

		#connects socket to address
		client.connect(address)

		#message prompt, quits on "exit"
		message = raw_input("Enter an operator and two numbers, in that order delimited by spaces (\'exit\' to disconnect): ")
		if message.lower() == "exit":
			client.close()
			break

		#socket sends message to address
		client.send(message)

		#reponse recieved from address
		response = client.recv(1024).split(" ")

		#responses
		# I'm only leaving the "else" there in case you create some unhandled issue
		# that i have not seen and want to have some idea where you are.
		# I believe responses are partitioned by the first two
		if response[0] == "200":
			print "Status Code: ", response[0], "\nResponse: ", response[1]

		elif response[0] == "300":
			print "Status Code: ", response[0], "\nResponse: ", response[1], "\nMessage: ", " ".join(response[2:])
		else:
			print "This should never happen"
			print "rep[0]", response[0], " rep[1]", response[1]

		client.close()

if  __name__ == '__main__':
    main()

