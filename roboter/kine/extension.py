#!/usr/bin/python

import math


class Extension:
	
	def __init__(self, length):
		self.L = length


	#Translates the Coordinates from the original Coordinates, to the Joint of the extension
	def translateCoordinates(self, x, y, z, vecX, vecY, vecZ):
		factor = self.L / math.sqrt(vecX*vecX + vecY * vecY + vecZ* vecZ)
		self.jointX = x - (factor * vecX)
		self.jointY = y - (factor * vecY)
		self.jointZ = z - (factor * vecZ)
		
		return self.jointX, self.jointY, self.jointZ	
