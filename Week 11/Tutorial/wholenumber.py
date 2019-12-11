class WholeNumber(object):
	def __init__(self,number):
		if number >= 0:
			self.number = number
		else:
			print("Positive numbers only")
			self.number = 0
	def __str__(self):
		return str(self.number)
	def __add__(self,other):
		return self.number + other.number
	def __sub__(self,other):
		return self.number - other.number if self.number - other.number >= 0 else 0
	def __mul__(self,other):
		return self.number * other.number

x = WholeNumber(5)
y = WholeNumber(3)

print(x+y)
print(x-y)
print(y-x)
print(x*y)