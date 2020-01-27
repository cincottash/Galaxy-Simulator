from vpython import *
from galaxy import *
from globals import *
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

	Milkyway = Galaxy(10, 10, vector(0,0,0), vector(0,0,0))


if __name__ == '__main__':
	main()