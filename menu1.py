#!/usr/bin/python

import commands
import time
import os

option='''
press 1 to check internet cable on your machine.
press 2 to check internet access.
press 3 to check for google access.
'''
print " "
print "      *************************  "
print option 
print " "
choice=raw_input("Enter your choice: ")
b=commands.getoutput('hostname -I').split(' ')
ip=b[0]
print "  "
x=commands.getoutput('ifconfig | cut -d " " -f1')
y=x.split(':')
z=x.split('\n')
red=commands.getoutput('mii-tool '+y[0])
ubu=commands.getoutput('sudo mii-tool '+z[0])
re=commands.getoutput('cat /etc/redhat-release')
ub=commands.getoutput('cat /etc/issue')

if choice=='1':
	print "Plz wait internet cable is being checked ..."
	time.sleep(2)
	if "Red Hat" in re:
		print "		Checking In Redhat OS..."
		time.sleep(2)
		if "link ok" in red:
			print "		LAN Cable is Connected."
		elif ip=='192.168.122.1':
			print "		Niether LAN Cable Nor Wifi is Connected."
			print "		Kindly recheck the internet cable on your machine."
		else:
			print "		Wifi is Connected."
	elif "Ubuntu" in ub:
		print "		Checking In Ubuntu OS..."
		time.sleep(2)
		if "link ok" in ubu:
			print "		LAN Cable is Connected."
		elif ip=='192.168.122.1':
			print "		Niether LAN Cable Nor Wifi is Connected."
			print "		Kindly recheck the internet cable on your machine."
		else:
			print "		Wifi is Connected."
	else:
		print "		Please Use Either Redhat Or Ubuntu."
elif choice=='2':
	print "Trying to check the internet access:"
	time.sleep(2)
	if ip=='192.168.122.1':
		print "		Internet Cable Is Not Connected."
		print "		Kindly recheck the internet cable on your machine."
	else:
		print "ping 8.8.8.8"
		time.sleep(1)
		os.system('ping 8.8.8.8 -c 5')
		print " "
		time.sleep(2)
		print "		Internet Access is ALRIGHT !"		
elif choice=='3':
	print "Trying to check the Google Access ..."
	time.sleep(2)
	if ip=='192.168.122.1':
		print "		Internet Cable Is Not Connected."
		print "		Kindly recheck the internet cable on your machine."
	else:
		print "		Google Is READY !"
		time.sleep(2)
		commands.getoutput('firefox 172.217.166.164')
else:
	print "wrong choice."
	print "TRY AGAIN !"
