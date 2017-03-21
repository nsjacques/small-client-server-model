import socket

#create TCP socket object
#connect to a server
#send data to server
#recieve data

def main():
	while(True):

		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ip=socket.gethostbyname(socket.gethostname())
		port = 50001
		address=(ip, port)

		client.connect(address)

		message = raw_input("Enter an operator and two numbers, in that order delimited by spaces (\'exit\' to disconnect): ")
		if message.lower() == "exit":
			client.close()
			break
		client.send(message)

		response = client.recv(1024).split(" ")

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

