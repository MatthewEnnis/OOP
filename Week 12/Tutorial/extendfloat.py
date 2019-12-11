class Par(float):
	def __str__(self):
		return "{}{}".format(float.__str__(self)," (" + self.name + ")" if self.name else "") 

a = Par(1.1)
a.name = "alpha"

b = Par(2.2)
b.name = "beta"

t = [1,2,b,a,a+b,a*b,a/b]

print(t)
t.sort()
for s in t:
	print(s)