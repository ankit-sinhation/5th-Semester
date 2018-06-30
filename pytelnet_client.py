#!/usr/bin/python

import socket,commands

'''
#		CODE FOR SERVER !
#		type of ip  ,  type of protocol UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind current and port
#		IP	 port
s.bind(("192.168.10.182",8000))

# 	buffer size	that means data recve by per client as single send.
for i in range(10000):
	data=s.recvfrom(100)
	if 'data' in data[0]:
		print commands.getoutput('date')
	elif 'cal' in data[0]:
		print commands.getoutut('cal')
	else:
		print data

'''

#		CODE FOR CLIENT !

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(10000):

	cmd=raw_input("Enter any linux command:  ")
	s.sendto(cmd,("192.168.10.182",8000))





