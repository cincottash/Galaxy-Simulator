import random
from star import *
class Galaxy():

	def __init__(self, numStars, radius, color):
		self.radius = radius
		self.pos = vector(0,0,0)
		self.velocity = vector(0,0,0)
		self.numStars = numStars
		self.color = color
		self.mass = 0

		self.starList = []
		#TODO: ADD A SUN
		#self.starList.append(Star(7, 7, vector(self.pos.x, self.pos.y, self.pos.z), self.color))
		for i in range(numStars):
			#scatter the stars within the galaxy's radius
			massRadius = random.randint(1, 5)
			self.starList.append(Star(massRadius, massRadius, vector(self.pos.x+random.randint(-radius, radius)/radius*radius, self.pos.y+random.randint(-radius, radius)/radius*radius, self.pos.z+random.randint(-radius, radius)/radius*radius), self.color))
			self.mass += self.starList[i].mass

		

