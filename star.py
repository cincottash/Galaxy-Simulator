from vpython import *
class Star(object):
	def __init__(self, mass, radius, pos, vel):
		self.obj = sphere(pos = pos, radius = radius)
		self.mass = mass
		self.radius = radius
		self.vel = vel
		self.pos = pos
		