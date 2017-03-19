import socket

#create TCP socket object
#connect to a server
#send data to server
#recieve data


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ?
ip=socket.gethostbyname(socket.gethostname())
port = 50001
address=(ip, port)

client.connect(address)

while(True):
	data_out = raw_input("Enter an operator and two numbers, in that order delimited by spaces: ")

	client.send(data_out)

	data_in = client.recv(1024)

	try:
		print "Result", int(data_in)
	except ValueError:
		print data_in
		if data_in == "Goodbye":
			break


client.close()

