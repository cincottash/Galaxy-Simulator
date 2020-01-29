from globals import *
from star import *
from galaxy import *



def calculateStarForce(galaxyA):
	for i in range(len(galaxyA.starList)):
		for j in range(len(galaxyA.starList)):
			#dont calculate force on itself
			if(galaxyA.starList[i] != galaxyA.starList[j]):
				#do force calculation here
				print("hello")
		#Change acceleration/velocity here

		galaxyA.starList[i].acceleration.x += dt
		galaxyA.starList[i].acceleration.y += dt
		galaxyA.starList[i].acceleration.z += dt

		galaxyA.starList[i].velocity.x += galaxyA.starList[i].acceleration.x
		galaxyA.starList[i].velocity.y += galaxyA.starList[i].acceleration.y
		galaxyA.starList[i].velocity.z += galaxyA.starList[i].acceleration.z
	
	#update positions AFTER finding all the new velocities so we can update the planets all at once
	for i in range(len(galaxyA.starList)):
		print("third for loop")
		galaxyA.starList[i].obj.pos.x += dt
		galaxyA.starList[i].obj.pos.y += dt
		galaxyA.starList[i].obj.pos.z += dt

def main():
	time = 0
	dt = 0.01
	'''
	star = Star(2, 1, vector(0,0,0), vector(1,0,0))
	acceleration = vector(1,0,0)
	
	while(time<100):
		rate(100)
		star.vel += acceleration*dt
		#use.obj to refrence the sphere
		star.obj.pos += star.vel*dt
		time += dt

	'''


	#TODO: Make the stars move in ONE galaxy first, then add the second galaxy and see what happens

	Milkyway = Galaxy(numStars, galaxyRadius, color.red)
	#Andromeda = Galaxy(numStars, galaxyRadius, andromedaPos, initialVelocity, color.blue)

	while time < 100:
		rate(100)
		#print("working")	
		calculateStarForce(Milkyway)
		time += dt
	
	


if __name__ == '__main__':
	main()