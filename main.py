from vpython import *
from galaxy import *
from star import *

def main():
	
	star = Star(2, 1, vector(0,0,0), vector(1,0,0))
	t = 0
	dt = 0.01
	acceleration = vector(1,0,0)
	

	while(t<100):
		rate(100)
		star.vel += acceleration*dt
		#use.obj to refrence the sphere
		star.obj.pos += star.vel*dt
		t += dt



if __name__ == '__main__':
	main()