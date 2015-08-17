'''
Created on Jun 5, 2015

@author: bharathm

File: testconnectivity.py
Description: The program reads an array of host,port and attempts an telnet session to it. The telnet session is connected and established until it reads an Escape in the telnet interaction, once it does it sends and exit and closes the telnet session.

To run this program, use the following command, remember to use python2.6 and above
/usr/bin/python2.6 testconnectivity.py


ToDo:
Read the opswiki page for that service, get the details of the connectivity map section, parse and attempt telnet 
There could be different hosts which prefer different types of network connectivity such as telnet, socket read/write, udp, http GET/PUT/POST, etc



How a successful run looks like:
================================
[g2wapistagebr1.expertcity.com', 8080]
Attempting telnet to:g2wapistagebr1.expertcity.com at Port:8080
Connected successfully.


If the telnet connection is unsuccessful then there will be errors printed to the stdout.

Attempting telnet to:api.mixpanel.com at Port:443
Traceback (most recent call last):
  File "testconnectivity.py", line 40, in <module>
    tn=telnetlib.Telnet(myList[0], myList[1], host_telnet_timeout)
  File "/usr/lib64/python2.6/telnetlib.py", line 209, in __init__
    self.open(host, port, timeout)
  File "/usr/lib64/python2.6/telnetlib.py", line 225, in open
    self.sock = socket.create_connection((host, port), timeout)
  File "/usr/lib64/python2.6/socket.py", line 561, in create_connection
    raise error, msg
socket.timeout: timed out


'''

import sys
import telnetlib
import json
import datetime
#from telnetlib import TELNET_PORT



##### Variables #####
postfix_hostname=".expertcity.com"
host_telnet_timeout=1  #in seconds


#Add your hosts here and ports 
host_port_array_g2wbroker=[
  #[hostname or IP, port]
  ["global.gotowebinar.com", 80],
  ["global.gotowebinar.com", 443],
  ["attendee.gotowebinar.com", 80],
  ["attendee.gotowebinar.com", 443],
  ["app.gotowebinar.com", 443],
  ["secure.citrixonline.com", 443],
  ["api.mixpanel.com", 80],
  ["audiov2svc.las"+postfix_hostname, 80],
#  ["accsvc.las"+postfix_hostname, 8085],
#  ["accsvc.iad"+postfix_hostname, 8085],
  ["arcsvc.las"+postfix_hostname, 80],
  ["msgsvc.las"+postfix_hostname, 80],
  ["queuesvc.las"+postfix_hostname, 80],
  ["queuesvc.iad"+postfix_hostname, 80],
  ["couchdb.iad"+postfix_hostname, 5984],
  ["svc2racdb-scan.iad"+postfix_hostname, 1521]
]

host_port_array_g2wattendee=[
  #[hostname or IP, port]
  ["queuesvc.las"+postfix_hostname, 80],
  ["queuesvc.iad"+postfix_hostname, 80],
  ["arcsvc.las"+postfix_hostname, 80],
  ["logstore.ops"+postfix_hostname, 11111],
  ["logstore.ops"+postfix_hostname, 22222]
]


print "###################################################"
print "Start run at:" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"


for host_a in range(len(host_port_array_g2wbroker)):
  print host_port_array_g2wbroker[host_a]
  myList=host_port_array_g2wbroker[host_a]

  print "Attempting telnet to:" + myList[0] +" at Port:" + `myList[1]` 
  tn=telnetlib.Telnet(myList[0], myList[1], host_telnet_timeout)
  print "Connected successfully."
  #tn.set_debuglevel(3)
  data=tn.read_until("Escape*", 5)
  print data

  tn.write("exit\n")
  tn.close()
  print "Closed telnet session."


print "End run at:" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print "###################################################" +"\n"
