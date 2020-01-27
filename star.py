from vpython import *

class Star(object):
	def __init__(self, mass, radius, pos, velocity):
		self.obj = sphere(pos = pos, radius = radius)
		self.mass = mass
		self.radius = radius
		self.velocity = velocity
		self.pos = pos
	
