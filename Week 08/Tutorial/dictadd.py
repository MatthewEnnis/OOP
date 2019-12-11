d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}

d3 = d1
for key in d2:
	if key in d3:
		d3[key] += d2[key]
	else:
		d3[key] = d2[key]

print(d3)