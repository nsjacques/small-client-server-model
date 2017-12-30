# Networks 453 Programming Project

## Description

This is a small, almost toy project for a networks class early 2017.

I wrote 3 server/client pairs using Python 2.7.10. One using TCP as the underlying transport protocol and two that use UDP. The two using UDP differ in their reliability. One handles dropped packets (neither handles corrupt segments).

### ServersEach server does the same thing: returns the result of some operation on two numbers, all three of which are provided by a user of the server’s corresponding client software.Each works similarly: when a server is started it creates a socket on its machine and binds this socket to an IP address and port number.The TCP server then listens for at most one connection, connects when it receives it, receives and handles that data, responds to the client and requests the TCP connection be closed. It then waits for new connection requests.After binding, the UDP servers receive, handle, and respond to data. The UDP server with dropped packet protections will drop 50% of the packets it receives, so one can test its corresponding client while running them on the same machine.There is some output server-side so one can easily follow what is happening.
### ClientsClients with absolute connections create a socket and connect it to the server. They prompt the user for input (offering an exit code). The exit code terminates the client, otherwise the input is sent to the server. The client receives a response code (200, 300) with a message (result, error). Then the client closes. The TCP client loops around to support multiple connections in one session.Clients with risky connections create a socket and connect it to the server. They prompt the user for input (offering an exit code). The exit code terminates the client, otherwise the input is sent to the server. The client waits 0.1s and for a response and if one is not received, it resends and waits double the time. If this interval grows to 2 or more seconds, the client reports a timeout and quits. Otherwise, the client receives a response code (200, 300) with a message (result, error). Then the client closes.

### Design TradeoffsI chose to hard-code the port numbers instead of asking the user for them. I prompted the user initially, however when I was testing rapidly I changed it to be hard-coded. This is an easy fix, but not particularly important to the assignment itself.
### Preconditions to the programs:The hard-coded port #s must be available on the machine.The server must be running before the client attempts to connect.Sending more than 1024 bits of info (this should never happen, the nature of the program).
### What does not work:Neither UDP pair handles corrupted or out-of-order data. See preconditions.

### Possible ImprovementsHave the reliable UDP pair handle corrupt and out-of-order information. This can be done using checksums and sequence numbers.
Automate more complex testing.

## File info 

#### File listing:

##### TCP:

TCP_client.py
TCP_server.py

##### UDP with timeout detector:

UDP_client_safeguard.py
UDP_server_safeguard.py

##### UDP without timeout detector:

UDP_client_noSafeguard.py
UDP_server_noSafeguard.py

#### Running

All written in Python 2.7.10

Can be run with the following command: python <filename.py>

Run server and then run corresponding client.

## Project Report### Testing
I ran similar tests for each program.#### Valid InputThe input is a string. Any string with fewer than 3 spaces is detected as invalid and handled, shortly afterwards any string with more than 3 is invalid and handled.Now all input is an array of 3 strings. If the latter two are not integers, the request is invalid and handled. If the first is not a valid operation code, it is invalid and handled.So now all input has a proper OC, and two integers. The only thing that can go wrong here is division by zero, and this is handled by the code that deals with division.
#### Testing UDP with dropping packets:Ran all of the above tests a number of times sufficient to ensure packets were dropping and being handled properly.
#### Etc


