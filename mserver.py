from socket import *
msg=''
data=''
TO_ADDR=('198.168.1.103',8138)
hostname=gethostbyname('0.0.0.0')
LOCAL_ADDR=(hostname,8135)
MSG_LEN=1000
fd=socket(AF_INET,SOCK_DGRAM)
fd.bind(LOCAL_ADDR)

def recv():
	msg,addr=fd.recvfrom(MSG_LEN)
	print '\nclient:',msg
	#print '\n'
	return msg,addr
def send(msg,addr):
	#fd.connect(('198.168.1.103',8138))
	fd.sendto(msg,addr)
	


while data!='stop' or msg!='stop':
	data,addr=recv()
	msg=raw_input('Enter your message:')
	send(msg,addr)



























