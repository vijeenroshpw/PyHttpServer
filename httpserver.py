import os,socket,sys

SERVER_ROOT ='/var/www'
print "\n\n\n              ###  Vijeen Http Server ###  \n       Author : Vijeenrosh P.W <hsorhteeniv@gmail.com> \n             Licenced under GNU Public Lisence\n\n\n"

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost',8000))
s.listen(1)
def reap_the_child():
	while 1:
		try:
			res = os.waitpid(-1,os.WNOHANG)
			if not result[0]:                                                    #means no process are currently zombie
				break
		except:	
			break

while 1:
	#try:
	clientsock,clientaddr = s.accept()
	
	#except:
		#print " Some error have occured "

	reap_the_child()
	
	pid = os.fork()
	if pid:
		clientsock.close()     #main server donot need the client sock , so close it
 		continue
	else:
		s.close()                   # child donot need the server connection object so close it away
		request = clientsock.recv(4096)
		print request.split("\n")[0]
		
		buff = request.split()[1]
		PATH = SERVER_ROOT + buff
		
				
		try:		
			fp = open(PATH,'r')
			data = fp.read()	
				
			clientsock.sendall(data)
			fp.close()
		except:
			pass
				
		#clientsock.sendall(data)
		#fp.close()		
		#print PATH
		clientsock.close()
		sys.exit(0)
		
	
