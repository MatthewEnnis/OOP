class BankAccount:
	def __init__(self):
		self.balance = 0
	def withdraw(self,amount):
		self.balance -= amount
		return self.balance
	def deposit(self,amount):
		self.balance += amount
		return self.balance

class MinimumBalanceAccount(BankAccount):
	def __init__(self,minimum):
		BankAccount.__init__(self)
		self.minimum = minimum
	def withdraw(self, amount):
		if self.balance - amount > self.minimum:
			self.balance -= amount
		else:
			print("Not enough money to withdraw :(")
		return self.balance

your_account = BankAccount()
print(your_account.deposit(10))
print(your_account.withdraw(20))

my_account = MinimumBalanceAccount(5)
print(my_account.deposit(10))
print(my_account.withdraw(20))