from vpython import *

class Star():
	def __init__(self, mass, radius, pos, velocity, color):
		self.obj = sphere(pos = pos, radius = radius, color = color)
		self.mass = mass
		self.radius = radius
		self.velocity = velocity
		self.pos = pos
		self.color = color
	
