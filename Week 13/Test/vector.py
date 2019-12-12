import math

class Vector3D(object):
	"""
	A class which stores a 3D vector with an x, y, and z
	"""
	def __init__(self,x,y,z):
		"""
		Initializes the x, y, and z
		"""
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
	
	def __str__(self):
		"""
		Returns a string in the format:
		(x, y, z)
		"""
		return "({:f}, {:f}, {:f})".format(self.x,self.y,self.z)
	
	def __add__(self,other):
		"""
		Returns a vector made from adding two vectors in the format:
		(x1+x2,y1+y2,z1+z2)
		"""
		return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
	
	def __sub__(self,other):
		"""
		Returns a vector made from subtracting two vectors in the format:
		(x1-x2,y1-y2,z1-z2)
		"""
		return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
	
	def __mul__(self,other):
		"""
		Returns a vector
		if other is a vector it multiplies with the format:
		(x1*x2,y1*y2,z1*z2)
		if other is an int it multiplies with the format:
		(x*n,y*n,z*n)
		"""
		if type(other) == Vector3D:
			return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
		return Vector3D(self.x*other,self.y*other,self.z*other)
	
	def magnitude(self):
		"""
		Returns the magnitude of the vector found with the forumula:
		sqrt(x^2+y^2+z^2)
		"""
		return math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))

#Testing the class

#testing init
v1 = Vector3D(1,2,3)
v2 = Vector3D(5,5,5)

#testing print
print("Printing v1")
print("v1 = ",v1)
print("Printing v2")
print("v2 = ",v2)

#testing add
v3 = v1 + v2
print("Printing addition")
print("v1 + v2 = ",v3)

#testing sub
v4 = v1 - v2
print("Printing subtraction")
print("v1 - v2 = ",v4)

#testing dot product
v5 = v1 * v2
print("Printing dot product")
print("v1 * v2 = ",v5)

#testing integer multiplication
v6 = v1 * 2
print("Printing integer multiplication")
print("v1 * 2 = ",v6)

#testing magnitude
print("v1 magnitude is ",v1.magnitude())
