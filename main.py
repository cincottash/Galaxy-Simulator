from globals import *
from star import *
from galaxy import *
'''
def calculateStarForce(galaxyA):
	for star in range(len(galaxyA.starList)):
		if(star != galaxyA.starList[i]):
			print("hello world!")
'''
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


	
	Milkyway = Galaxy(numStars, galaxyRadius, milkywayPos, initialVelocity, color.red)
	


	#Andromeda = Galaxy(numStars, galaxyRadius, andromedaPos, initialVelocity, color.blue)
	#print(Milkyway.starList[0])
	#TODO: Make the stars move in ONE galaxy first, then add the second galaxy and see what happens


if __name__ == '__main__':
	main()