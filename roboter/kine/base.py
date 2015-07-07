#!/usr/bin/python
import math

class Base:

	def __init__(self, diameter):
		self.Diameter = diameter	

	# Calculates to which position the Base has to turn
	def calcBaseDegrees(self, x, y):
		degrees = 0
		if (y == 0):
			if (x >= 0):
				degrees = 90
			else:
				degrees = -90
		else:
			degrees = math.degrees(math.atan(x/y))
			if (x < 0 and y > 0):
				#oberer Linker Quadrant
				degrees += 360
			elif (y < 0):
				#untere Quadranten
				degrees += 180
		return degrees
	
	# Translates the absolute X Y Z Coordinates into the Relative X and Z Coordinates for the arm calculations
	def translateCoordinates(self, x, y, z):
		# X, Y span the ground plane
		# calculate the length of the groundLine
		groundLine = math.sqrt(x ** 2 + y ** 2)
		# calculate Length and Degree (to groundPlane) of the room diagonal
		roomDiagonal = math.sqrt(groundLine ** 2 + z ** 2)
		roomDegrees = math.degrees(math.atan(z/groundLine))
		groundLine = groundLine - self.Diameter
		return groundLine, 0, z

	# Calculates in which direction the Base has to turn for the shortest way
	def calcBaseMovement(self, newDegrees, oldDegrees):
		deg = 0
	
		if (newDegrees > ( (oldDegrees + 180 )% 360)):
			#turn anti clockwise
			deg = -1 * (math.fabs(oldDegrees - newDegrees))
			if (deg < -180):
				deg += 180
		else:
			#turn clockwise
			deg = math.fabs((oldDegrees - newDegrees))
			if (deg > 180):
				deg -= 180
		return deg
