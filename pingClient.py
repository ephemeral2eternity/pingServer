#!/usr/bin/env python
import socket
import time

ip = "127.0.0.1"
port = 8717
# Connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Send the data
message = 'PING'
# print 'Sending : "%s"' % message
ts_sent = time.time()
len_sent = s.send(message)

# Receive a response
response = s.recv(len_sent)
ts_recv = time.time()
# print 'Received: "%s"' % response
rtt = (ts_recv - ts_sent) * 1000
print 'The RTT is : ' + str(rtt) + " ms"

# Clean up
s.close()