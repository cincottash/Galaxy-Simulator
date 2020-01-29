import random
from star import *
class Galaxy():

	def __init__(self, numStars, radius, pos, velocity, color):
		self.radius = radius
		self.pos = pos
		self.velocity = velocity
		self.numStars = numStars
		self.color = color
		self.mass = 0

		self.starList = []
		for i in range(numStars):
			#scatter the stars within the galaxy's radius
			self.starList.append(Star(10, random.randint(1, 3), vector(pos.x+random.randint(-radius, radius)/radius*radius, pos.y+random.randint(-radius, radius)/radius*radius, pos.z+random.randint(-radius, radius)/radius*radius), self.color))
			self.mass += self.starList[i].mass

		

