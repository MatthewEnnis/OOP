def gcd(bigger,smaller):
	while smaller > 0:
		bigger, smaller = smaller, (bigger % smaller)
	return bigger

def lcm(first,second):
	if first > second:
		return (first*second)//gcd(first,second)
	return (first*second)//gcd(second,first)

def addFrac(frac1,frac2):
	comdom = lcm(frac1[1],frac2[1])
	return frac1[0]*comdom//frac1[1]+frac2[0]*comdom//frac2[1],comdom

def subFrac(frac1,frac2):
	comdom = lcm(frac1[1],frac2[1])
	return frac1[0]*comdom//frac1[1]-frac2[0]*comdom//frac2[1],comdom

def reduce(frac):
	if frac[0] > frac[1]:
		div = gcd(frac[0],frac[1])
	else:
		div = gcd(frac[1],frac[0])
	return frac[0]//div,frac[1]//div

def allFunc(frac1,frac2):
	print()
	print(frac1,"+",frac2,"=",reduce(addFrac(frac1,frac2)))
	print(frac1,"-",frac2,"=",reduce(subFrac(frac1,frac2)))
	print(frac2,"-",frac1,"=",reduce(subFrac(frac2,frac1)))
	
def getFrac(fracname):
	print("\n"+fracname+":\n")
	return int(input("Please enter the top number: ")),int(input("Please enter the bottom number: "))

frac1 = getFrac("Fraction 1")
frac2 = getFrac("Fraction 2")

allFunc(frac1,frac2)
