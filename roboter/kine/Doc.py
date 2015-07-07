def Script_1():
	#importieren der benoetigten module
	import VR
	import math
	import sys
	sys.path.append("myMod")
	
	#importieren von dem Modul
	from myMod import arm, base, extension
	reload(arm)
	reload(base)
	reload(extension)
	
	j0 = VR.getRoot().find('j0')
	j1 = VR.getRoot().find('j1')
	j2 = VR.getRoot().find('j2')
	x = 3
	y = 4
	z = 5
	vecX, vecY,vecZ= 0,1,0
	
	#Arm mit armlängen erstellen (unterer Arm, oberer arm)
	arm = arm.Arm(4,5)
	#base erstellen mit abstand des armgelenkes zum mittelpunkt
	base = base.Base(3)
	#armverlängerung erstellen mit länge
	extension = extension.Extension(3)
	
	x, y, z = extension.translateCoordinates(x, y, z, vecX, vecY, vecZ)
	
	#berechnen des basiswinkels
	baseDegrees = base.calcBaseDegrees(x, y)
	
	#transformieren der X Coordinate von absolut auf relativ zum arm
	relX = base.translateCoordinates(x, y, z)
	
	#berechnen der armwinkel
	alpha, beta , delta= arm.calculateArmDegrees(x, z)
	
	#berechnung der armbewegung , berechnet eig. nur die differenz)
	alphaDeg, betaDeg = arm.calcArmMovement(oldAlpha, oldBeta, alpha, beta )
	
	print alpha, beta, delta
	
