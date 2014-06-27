from socket import *
import sys
import time
TO_ADDR=('192.168.1.104',8135)
hostname=gethostbyname('0.0.0.0')
LOCAL_ADDR=(hostname,8138)
MSG_LEN=1000
fd=socket(AF_INET, SOCK_DGRAM)
fd.bind(LOCAL_ADDR)
addr=TO_ADDR

data=''
msg=''
def recv():
	data,addr=fd.recvfrom(MSG_LEN) 
	print '\nserver:',data
	#print '\n'
	return data,addr
def send(msg,addr):
	#fd.connect(('192.168.1.101',8135))
	fd.sendto(msg,addr)
	
while msg!='stop'  and data!='stop':
	print '\n'
	msg=raw_input('Enter your message:')
	send(msg,addr)	
	data,addr=recv()
	























