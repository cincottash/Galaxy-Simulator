from vpython import *
import random

class Star():
	def __init__(self, mass, radius, pos, color):
		self.pos = vector(pos.x+random.randint(-radius, radius)/radius*radius, pos.y+random.randint(-radius, radius)/radius*radius, pos.z+random.randint(-radius, radius)/radius*radius)
		self.obj = sphere(pos = self.pos, radius = radius, color = color)
		self.mass = mass
		self.radius = radius
		self.velocity = vector(0,0,0)
		self.acceleration = vector(0,0,0)
		self.color = color

	
