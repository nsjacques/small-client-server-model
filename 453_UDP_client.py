import socket

data_out = raw_input("Enter an operator and two numbers, in that order delimited by spaces: ")
address = ( socket.gethostbyname(socket.gethostname()), 50010 )

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(data_out, address)

client.close()