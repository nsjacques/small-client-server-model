import socket

#create TCP socket object
#connect to a server
#send data to server
#recieve data

def main():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ?
	ip=socket.gethostbyname("www.google.com")
	port = 80
	address=(ip, port)

	client.connect(address)
	client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
	data = client.recv(1024)

	print data

	#raw_input() ?


if  __name__ == '__main__':
    main()