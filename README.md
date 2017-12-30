# Networks 453 Programming Project

## Description

This is a small, almost toy project for a networks class early 2017.

I wrote 3 server/client pairs using Python 2.7.10. One using TCP as the underlying transport protocol and two that use UDP. The two using UDP differ in their reliability. One handles dropped packets (neither handles corrupt segments).

### Servers


### Design Tradeoffs
### Preconditions to the programs:


### Possible Improvements
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

## Project Report
I ran similar tests for each program.



