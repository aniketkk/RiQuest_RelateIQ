#!/usr/bin/python
import sys
import math
class Robot:
#***************** i have defined four  data attributes to define position of the robot*********
 	
	def __init__(self,current_orientation ='N', orientation_value = 0.0, x_coordinate = 0.0, y_coordinate=0.0):
		self.current_orientation = current_orientation
		self.orientation_value = orientation_value
		self.x_coordinate = x_coordinate
		self.y_coordinate = y_coordinate

#******************************** end of init ***************************************************

#*********** update position/orientation based on input received from the string ****************
	
	def action(self, input, x_coordinate, y_coordinate):
		if input == 'C':
			self.orientation_value += 45.0
			#print "Orientn:	"+str(self.orientation_value)
		if input == 'A':
			self.orientation_value -= 45.0
			#print "Orientn: "+str(self.orientation_value)
		if input == 'S':
			#print "S:	"+str(float(self.orientation_value*math.pi)/180.0)
			self.x_coordinate = self.x_coordinate + 1.0*math.sin(self.orientation_value*3.142/180.0)

			self.y_coordinate = self.y_coordinate + 1.0*math.cos(self.orientation_value*3.142/180.0)
			x_avg =  (math.floor(self.x_coordinate) + math.ceil(self.x_coordinate)) / 2.0 
			y_avg =  (math.floor(self.y_coordinate) + math.ceil(self.y_coordinate)) / 2.0 
			if self.x_coordinate < x_avg:
				self.x_coordinate = math.floor(self.x_coordinate)
			else:
				self.x_coordinate = math.ceil(self.x_coordinate)
			
			if self.y_coordinate < y_avg:
                                self.y_coordinate = math.floor(self.y_coordinate)
                        else:   
                                self.y_coordinate = math.ceil(self.y_coordinate)

#******************************** end of action *************************************************

#*************************** output the final orientation as a direction ************************

	def  orientation(self, orientation_value):
		if math.fabs(self.orientation_value%360.0) == 0.0:
			return 'N'	
		if math.fabs(self.orientation_value%360.0) == 45.0:
			return 'NE'
		if math.fabs(self.orientation_value%360.0) == 90.0:
			return 'E'
		if math.fabs(self.orientation_value%360.0) == 135.0:
			return 'SE'
		if math.fabs(self.orientation_value%360.0) == 180.0:
			return 'S'
		if math.fabs(self.orientation_value%360.0) == 225.0:
			return 'SW'
		if math.fabs(self.orientation_value%360.0) == 270.0:
			return 'W'
		if math.fabs(self.orientation_value%360.0) == 315.0:
			return 'NW'
#********************************end of orientation********************************************

#***** read from standard input *************
robot_actions = sys.stdin.readline()
#***create an instance of the Robot class****
robot_instance = Robot()
i = 0
for i in range(0, len(robot_actions)):
	robot_instance.action(robot_actions[i], robot_instance.x_coordinate, robot_instance.y_coordinate)
	final_orientation = robot_instance.orientation(robot_instance.orientation_value)

#******write to stdout*********
sys.stdout.write(str(int(robot_instance.x_coordinate))+" "+str(int(robot_instance.y_coordinate))+" "+final_orientation+"\n")

