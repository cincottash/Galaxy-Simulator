from star import *
import random

class Galaxy(object):

	def __init__(self, numStars, radius, pos, velocity):
		self.radius = radius
		self.pos = pos
		self.velocity = velocity
		self.numStars = numStars
		#self.color = color


		starList = []
		for i in range(numStars):
			starList.append(Star(10, 10, vector(random.randint(-radius, radius),random.randint(-radius, radius),random.randint(-radius, radius)), vector(0,0,0)))


