from vpython import *
import random

class Star():
	def __init__(self, mass, radius, pos, color):
		self.pos = pos
		self.obj = sphere(pos = self.pos, radius = radius, color = color)
		self.mass = mass
		self.radius = radius
		self.velocity = vector(0,0,0)
		self.acceleration = vector(0,0,0)
		self.color = color
		self.theta = 0
		self.distance = 0
		self.force = 0

	
