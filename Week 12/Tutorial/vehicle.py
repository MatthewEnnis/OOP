class Vehicle(object):
	def __init__(self,year=2019,vin=1,mileage=0):
		self.year = year
		self.vin = vin
		self.mileage = mileage
	def __str__(self):
		return "{} {}, mileage: {}".format(self.vin,self.year,self.mileage)
	def drive(self,distance=0):
		self.mileage += distance

class Car(Vehicle):
	def __init__(self,year=2019,vin=1,mileage=0,name="Car"):
		Vehicle.__init__(self,year,vin,mileage)
		self.name = name
	def __str__(self):
		return "{} {}".format(self.name,Vehicle.__str__(self))

class Truck(Vehicle):
	def __init__(self,year=2019,vin=1,mileage=0,wheels=4):
		Vehicle.__init__(self,year,vin,mileage)
		self.wheels = wheels
	def __str__(self):
		return "{} wheel, {}".format(self.wheels,Vehicle.__str__(self))

the_car = Car(1999,123,555,"Mr Car")
print(the_car)

the_truck = Truck(2012,321,808,"Mr Truck")
print(the_truck)

the_truck.drive(101)
print(the_truck)