
import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

#Defining pins for Distance
pinTrigger = 17
pinEcho = 18
leftMotorSpeed = 0.6
rightMotorSpeed = 0.5
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)
robot = CamJamKitRobot()
forward = (-leftMotorSpeed, -rightMotorSpeed)
left = (0, -rightMotorSpeed)
right = (-leftMotorSpeed, 0)
#robot.value = forward
#print(robot.value)
#time.sleep(0.1)
#print('Robot is running forward')
#robot.value = left
#time.sleep(0.2)
#print('Robot is turning left')
#robot.value = right
#time.sleep(1)

wallDistance = 10.0

def test():
	str('Hello')
	return str

def start():
	robot.value = forward
#	time.sleep(2)
#	robot.stop()
#	exit(0)
def stop():
	robot.stop()

def howFarAmI ():
	while True:
		dist = sensor.distance * 100
		print(int(dist))	
		return dist
#dist = (str(distance))	
#distance = distance
#	print('current distance is ')
#	print(distance) #
#	return(dist)
#distance = sensor.distance * 100
#while True:
#	distance = sensor.distance * 100
#	print ("Distance before moving: %.1f cm" % distance)
#	robot.value = forward
#	time.sleep(1)
#	howFarAmI(distance)
#	robot.value = right
#	time.sleep(0.5)
#	robot.stop()
#	howFarAmI(distance)
	#exit(0)
#	time.sleep(0.1)
#	robot.value = forward
#	time.sleep(0.2)
#	if (distance > 30):
#		print ("Distance: %.1f cm" % distance)
#		robot.value = right
#		time.sleep(0.01)
##		robot.value = forward
##		time.sleep(0.1)
#		if (distance < 60):
##			print ('turning right')
#			robot.stop()
#			exit(0)
#		elif (distance > 60):
##			print ('turning left')
##			robot.value = left
#			time.sleep(0.01)
#			if (distance <50 and distance >30):
#				robot.value = left
#				time.sleep(0.01)
#				if (distance < 30):
#					print ('distance is less than 30, stopping the robot !!')
#					robot.stop()
#					exit(0)
#		
#
#	


#	if (distance > 20):
#	robot.value = forward
#		time.sleep(1)
#		robot.stop()
#		
#	if (distance > 50):
#		print ('robot is moving')
#		robot.value = forward
		#time.sleep(3)
#		if (distance <= 20):
#			print ('stop')
#			robot.stop()
#			exit(0)		

#forward = (-leftMotorSpeed, -rightMotorSpeed)
#left = (0, -rightMotorSpeed)
#right = (-leftMotorSpeed, 0)
#robot.value = forward
#print(robot.value)
#time.sleep(0.1)
#print('Robot is running forward')
#robot.value = left
#time.sleep(1)
#print('Robot is turning left')
#robot.value = right
#time.sleep(1)



#while True:
#	robot = CamJamKitRobot()

#print(time)
#time.sleep(5)
#robot.stop()
