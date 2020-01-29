from globals import *
from star import *
from galaxy import *
import math

#TODO: Make the stars move in ONE galaxy first, then add the second galaxy and see what happens
def calculateStarForce(galaxyA):
	#Loop through each star to find the force exerted on it (due to all the other stars, but not the star itself)
	for i in range(len(galaxyA.starList)):
		#Loop through the rest of the stars to find the force each one exterts on our current star (starList[i])
		for j in range(len(galaxyA.starList)):
			#dont calculate force of star on itself
			if(galaxyA.starList[i] != galaxyA.starList[j]):
				#do force calculation here

				galaxyA.starList[i].theta = diff_angle(galaxyA.starList[i].pos, galaxyA.starList[j].pos)
				distance = (galaxyA.starList[i].pos.x - galaxyA.starList[j].pos.x)**2 + (galaxyA.starList[i].pos.y - galaxyA.starList[j].pos.y)**2 + (galaxyA.starList[i].pos.z - galaxyA.starList[j].pos.z)**2
				galaxyA.starList[i].force += (6.67*galaxyA.starList[i].mass*galaxyA.starList[j].mass)/(distance * 1000000)

				#Change acceleration/velocity here
				galaxyA.starList[i].acceleration.x += galaxyA.starList[i].force * math.cos(galaxyA.starList[i].theta)
				galaxyA.starList[i].acceleration.y += galaxyA.starList[i].force * math.sin(galaxyA.starList[i].theta)
				galaxyA.starList[i].acceleration.z += galaxyA.starList[i].force * math.tan(galaxyA.starList[i].theta)

		galaxyA.starList[i].velocity.x += galaxyA.starList[i].acceleration.x/10000
		galaxyA.starList[i].velocity.y += galaxyA.starList[i].acceleration.y/10000
		galaxyA.starList[i].velocity.z += galaxyA.starList[i].acceleration.z/10000
	
	#update positions AFTER finding all the new velocities so we can update the planets all at once
	for i in range(len(galaxyA.starList)):
		print("third for loop")
		galaxyA.starList[i].obj.pos.x += galaxyA.starList[i].velocity.x
		galaxyA.starList[i].obj.pos.y += galaxyA.starList[i].velocity.y
		galaxyA.starList[i].obj.pos.z += galaxyA.starList[i].velocity.z

def main():
	time = 0
	dt = 0.1
	#print(vector(0,0,0) + vector(0,0,0))

	Milkyway = Galaxy(numStars, galaxyRadius, color.red)
	#Andromeda = Galaxy(numStars, galaxyRadius, andromedaPos, initialVelocity, color.blue)

	while time < 100:
		rate(100)
		#print("working")	
		calculateStarForce(Milkyway)
		time += dt
	
	


if __name__ == '__main__':
	main()