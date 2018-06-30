#!/usr/bin/python
import time,commands,webbrowser
menu='''
Press 1: To check current time and date:
Press 2: To scan all your MAC address in your current connected network:
Press 3: To shutdown your machine after 15 minutes:
Press 4: To search something on google:
Press 5: To logout your current machine:
Press 6: To shutdown all connected system in your current network:
Press 7: To update status in facebook:
Press 8: To list IP address of given website:
'''
print menu
choice=raw_input("Enter your choice: ")

if choice == '1':
	print "Current date and time is:  ",time.ctime()
elif choice == '2':
	print "The Connected MAC's Are...."
	print "		"
	print "		"
	z=commands.getoutput('arp-scan -I wlo1 -l | grep -i 192.168.')
	z=z.splitlines()
	t=[]
	for i in z :
		a=i.split('\t')
		t.append(a)
	for i in range(0,len(t)) :
		print t[i][1]
#elif choice == '3':
	
elif choice == '4':
	find=raw_input("Enter your query: ")
	webbrowser.open_new_tab("https://www.google.com/search?q="+find)
else:
	print "wrong choice"
	
	
