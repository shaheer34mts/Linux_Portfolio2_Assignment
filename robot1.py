
import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

#Defining pins for Distance
pinTrigger = 17
pinEcho = 18
leftMotorSpeed = 0.8
rightMotorSpeed = 0.8
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)
robot = CamJamKitRobot()
forward = (leftMotorSpeed, rightMotorSpeed)
right = (0, rightMotorSpeed)
left = (leftMotorSpeed, 0)

wallDistance = 40.0

def test():
	str('Hello')
	return str

def start():
	robot.value = forward
def stop():
	robot.stop()

def howFarAmI ():
	while True:
		dist = sensor.distance * 100
		print(int(dist))	
		return dist
while True:
	distance = sensor.distance * 100
	print ("Distance before moving: %.1f cm" % distance)
	robot.value = forward
	time.sleep(0.2)
	print ("went straight")
	dist2 = sensor.distance * 100
	if (dist2 > 10+ wallDistance):
		print ("went left")
		robot.value = left
		time.sleep (0.05)
		dist3 = sensor.distance * 100
		if (dist3  > 88):
			print ("went nested right")
			robot.value  = right
			time.sleep(0.05)
	elif (dist2 < wallDistance -10):
		print ("went outer right")
		robot.value = right
		time.sleep(0.05)
	else:
		print ("went else straight")
		robot.value = forward
	#	time.sleep(0.3)




















