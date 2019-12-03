import socket
from robot1 import *
host = '192.168.99.12' #'192.168.43.230'
port = 8080


START_ROBOT = "Robot is running "
STOP_ROBOT = "Robot is stopping" 
def setupServer():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket has been created")
	try:
		s.bind((host, port))
	except socket.error as msg:
		print (msg)
	print ("Socket  bind Complete")
	return s

def setupConnection():
	s.listen(1)   #1 person at a time is allowed
	conn, address =  s.accept()
	print ("Connected to : " + address[0] + ":" + str(address[1]))
	return conn

def dataTransfer(conn):
	while True:
		data = conn.recv(12000)
		data = data.decode('utf-8')
		dataMessage = data.split(' ', 1)
		command = dataMessage[0]
		if command == 'EXIT':
			print ('Our Client has left us :( ')
			break
		elif command == 'KILL':
			print ('server is shutting down !!')
			s.close()
			break
		elif command == 'getdist':
			getDist()
			reply = GET2() 
		elif command == 'start':
			start()
			reply = GET()
		elif command == 'stop':
			stop()
			reply = GET1()
		elif command == 'followwall':
			Wall_Follower()
			reply = GET()
		else:
			reply == 'Unknown Command'
# Send reply back to the client
		conn.sendall(str.encode(reply))
		print('Data has been sent !')
	conn.close()


def GET():
	reply = START_ROBOT
	return reply

def GET1():
	reply = STOP_ROBOT
	return reply

def GET2():
	dist = howFarAmI()
	storedValue2 = "The distance is :" + str(dist)
	return storedValue2

def getDist():
	reply = howFarAmI()
#	print (reply)
	return reply

def Wall_Follower():
        followWall()
        valuee = "Robot is trying to follow the wall (we think :P)"
        return valuee

s =  setupServer()
while True:
	try:
		conn = setupConnection()
		dataTransfer(conn)
	except:
		break
