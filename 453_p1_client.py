import socket

#create TCP socket object
#connect to a server
#send data to server
#recieve data


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ?
ip=socket.gethostbyname(socket.gethostname())
port = 50000
address=(ip, port)

client.connect(address)

data_out = raw_input("Enter an operator and two numbers, in that order delimited by spaces: ")

client.send(data_out)

data_in = client.recv(1024)

client.close()

print int(data_in)