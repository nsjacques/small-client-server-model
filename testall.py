import socket
import random

import TCP_client as tcp_cl
import TCP_server as tcp_sv
import UDP_client_reliable as udp_cl_r
import UDP_server_reliable as udp_sv_r
import UDP_client_unreliable as udp_cl_u
import UDP_server_unreliable as udp_sv_u

#
def test_TCP():
	tcp_sv.main()
	tcp_cl.main()

#the UDP where the app layer does not handle dropped packets
def test_UDP_unreliable():
	udp_sv_u.main()
	udp_cl_u.main()

#the UDP where the app layer handles dropped packets
def test_UDP_reliable():
	udp_sv_r.main()
	udp_cl_r.main()


def main():
	try:
		test_TCP()
		test_TCP_unreliable
		test_UDP_reliable
	except:
		print "ok"


if  __name__ == '__main__':
    main()