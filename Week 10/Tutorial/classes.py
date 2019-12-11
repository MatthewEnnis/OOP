class Rectangle(object):
	def __init__(self,length=1,width=1):
		self.length = length
		self.width = width
	def __str__(self):
		return "Length: {}, Width: {}".format(self.length,self.width)
	def area(self):
		return self.length * self.width
	def perimeter(self):
		return self.length * 2 + self.width * 2

class BankAccount(object):
	def __init__(self,iban,account):
		self.iban = iban
		self.account = account
		self.balance = 0
		self.transactions = []
	def __str__(self):
		return "Balance: {}\nPrevious transactions: {}".format(self.balance,self.transactions)
	def deposit(self,amount):
		self.balance += amount
		self.transactions.append("Deposited {}".format(amount))
	def withdraw(self,amount):
		self.balance -= amount
		self.transactions.append("Withdrew {}".format(amount))

my_rectangle = Rectangle(5,8)
print(my_rectangle)
print(my_rectangle.area())
print(my_rectangle.perimeter())

my_account = BankAccount(123,"Matthew")
my_account.deposit(20)
my_account.withdraw(10)
print(my_account)