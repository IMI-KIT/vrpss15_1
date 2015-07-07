#!/usr/bin/python

import math

def main():

	#Armlangen
	arm = Arm(5, 4, 3)
	
class Arm:

	def __init__(self, l1, l2, l3):
		self.L1 = l1
		self.L2 = l2
		self.L3 = l3

	def calculateArmDegrees(self, X, Y):
		X = X - self.L3	
		X = X * -1
		
		C2 = (X*X + Y*Y - self.L1*self.L1 - self.L2*self.L2)/(2 * self.L1 * self.L2)
		A1 = math.fabs(1 - (C2 * C2))
		S2 = math.sqrt(A1)
	
		K1 = self.L1 + self.L2 * C2
		K2 = self.L2 * S2

		theta = math.atan2( Y, X ) - math.atan2( K2 , K1)  #angle: theta * 180/pi  (fur alpha 180 - theta)
	
		psi = math.atan2( S2, C2)    #angle: psi * 180/pi  (fur Beta 180 - psi)
		
		alpha = 180 - (theta * 180 / math.pi)
		beta = 180 - ( psi * 180 / math.pi)
		print 'theta: ', theta, 'psi: ', psi, 'K1: ', K1, 'K2: ', K2
		delta = -1 * (alpha - beta)
		alpha = alpha - 90
		beta = beta - 90
		return alpha, beta, delta

	
	def calculateArmXY(self, alpha, beta):
		J1X =cos(alpha * math.pi /180)* self.L1
		J1Y =sin(alpha * math.pi /180)* self.L1
	
		J2X =cos((beta + alpha) * math.pi/180)* self.L2 + J1X
		J2Y =sin((beta + alpha)* math.pi/180)* self.L2 + J1Y
	
		return J2X, J2Y
	
	def calcArmMovement(self, oldAlpha, oldBeta, newAlpha, newBeta):
		#Do something
		diffAlpha = newAlpha - oldAlpha
		diffBeta = newBeta - oldBeta

		return diffAlpha, diffBeta
main()
