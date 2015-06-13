# Versuch alle Winkel zu berechen die von w1 bis w5 für die Arme 1 bis 5 gelten
# Die winkel die Am ende raus kommen sind absolut für die Animation muss noch das Delta ausgerechnet werden
#Roboter steht auf der X-Y-Ebene

import math


l_a1 = 2.60145
l_a2 = 6.79983
l_a3 = 5.4269397999999995
l_a4 = 4.63536

z_offset_a2 = 6.75180

#Offset von w2 ergibt sich durch die länge
w2_offset = math.degrees(math.atan(l_a3/l_a2))
print("w2_offset:", w2_offset)


#input 
# Ziel Position pos = [x , y, z]
# Richtung des anfahrens  dir = [x, y, z]
# Ausrichtung Greifter nach oben up = [x, y, z]
pos = [12.66375, 0, z_offset_a2 + l_a3]
dir = [1, 0, 0]
up = [0, 0, 1]

print("pos:", pos , "\ndir:", dir)


#Länge Vector berechnen
def lenVec(inVec):
    return math.sqrt( sum(i * i for i in inVec))

#Vektor normalisieren
def normVec(inVec):
    leng = lenVec(inVec)
    outVec = inVec[:]
    for i in range(len(outVec)):
         outVec[i] = outVec[i]/leng
    return outVec

#Vector strecken
def streckenVec(inVec, faktor):
    n = 0
    outVec = inVec[:]
    for i in range(len(outVec)):
        outVec[i] *= faktor
    return outVec




#Schritt 0 Winkel w1 berechen
if pos[0] == 0 :
    w1 = 90
else :
    w1 = math.degrees(math.atan(float(pos[1])/float(pos[0])))
    if bool(pos[0] < 0) ^ bool(pos[1] < 0):
        w1 += 180 
w1 %= 360
print("Winkel 1 :" , w1)

#Schritt 1 Koordinaten für den Punkt anpassen
pos[0] -= (math.cos(math.radians(w1)) * l_a1)
pos[1] -= math.sin(math.radians(w1)) * l_a1
pos[2] -= z_offset_a2
print("angepasstes pos:",pos)


#Schrit 2.1 Position für ende von Arm2 ausrechnen
diff_vec = streckenVec(normVec(dir), l_a4)
print("diff_vec:", diff_vec)
a2_pos = [pos[0]-diff_vec[0], pos[1] - diff_vec[1], pos[2] - diff_vec[2]]
print("Position ende A2:" , a2_pos)

#Schritt 2.2 Winkel für die Schreckung berechnen
dist = lenVec(a2_pos)
print("dist:", dist)
##########################################
# hier plausibel
###########################################
#Consinus satz
pre_w2 = math.acos((-math.pow(l_a2,2) - math.pow(dist, 2) + math.pow(l_a3, 2))/(-2 * l_a2 * dist)) 
w3 = math.degrees(math.asin((math.sin(pre_w2) * dist)/l_a3)) 
#Da 90° beim Roboter 0° sind
w3 -= 90 
pre_w2 = math.degrees(pre_w2)
print("pre_w2 : ", pre_w2)

#Schritt 2.3 Entgültigen Winkel w2 für Arm 1 berechen
w2 = pre_w2 - w2_offset
w2 += math.degrees(math.atan(a2_pos[2]/(math.sqrt(math.pow(a2_pos[0],2) + math.pow(a2_pos[1],2)))))
print("Winkel w2 :" , w2)

#Schritt 3  up Vektor, einbauen (im Moment nicht unterstützt)
w4 = 0

#Schritt 4 
w5 = (w2 + (w3 + 90) ) -180     # gerade machen
# plus z-Achse ausgleichen
w5 += math.degrees(math.atan(diff_vec[2]/(math.sqrt(math.pow(diff_vec[0],2) + math.pow(diff_vec[1],2)))))
print("Winkel 5:", w5)

print("\n\nWinkel 1:", w1, "\nWinkel 2:", w2, "\nWinkel 3:", w3, "\nWinkel 4:", w4, "\nWinkel 5:", w5)
