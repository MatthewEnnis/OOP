#!/usr/bin/python3

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request

VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
					'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

class Currency:
	def __init__(self, amount=1, currency_type='EUR'):
		# a quick and easy way of checking for valid currencies
		# for a limited subset of valid currencies
		if currency_type in VALID_CURRENCIES:
			self.amount = amount
			self.currency_type = currency_type
		else:
			print("Invalid currency type: {}\n".format(currency_type))
			self.amount = 0
			self.currency_type = ''

	def convert_to(self, new_currency_type):
		if new_currency_type == self.currency_type:
			# nothing to do
			return Currency(self.amount, self.currency_type)

		if new_currency_type not in VALID_CURRENCIES or self.currency_type not in VALID_CURRENCIES:
			print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
			return

		# prepare URL
		url = "https://api.exchangeratesapi.io/latest?base="
		url += self.currency_type
		url += "&symbols=" + new_currency_type
		conv = urllib.request.urlopen(url)
		# read() returns an array of bytes, we want a string
		response = str(conv.read())

		# Extract the exchange rate from the variable 'response' and finish the implementation of the method.
		# The return is given. Amount is the the correct converted amount that needs to be found

		rate = float(response[18:response.find("}")])
		amount = self.amount * rate

		print("{:.2f} {} => {:.2f} {}".format(self.amount, self.currency_type, amount, new_currency_type))
		return Currency(amount, new_currency_type)

	def __str__(self):
		return "{:.2f} {}".format(self.amount, self.currency_type)

	def __repr__(self):
		return self.__str__

	def __add__(self, other_curr):
		if type(other_curr) == int or type(other_curr) == float:
			other_curr = Currency(other_curr,self.currency_type)
			
		if type(other_curr) == Currency:
			other_curr = other_curr.convert_to(self.currency_type)
			return Currency(self.amount+other_curr.amount,self.currency_type)
			
		print("Invalid type")
		return self

	def __sub__(self, other_curr):
		if type(other_curr) == int or type(other_curr) == float:
			other_curr = Currency(other_curr,self.currency_type)
			
		if type(other_curr) == Currency:
			other_curr = other_curr.convert_to(self.currency_type)
			return Currency(self.amount-other_curr.amount,self.currency_type)
			
		print("Invalid type")
		return self

	def __radd__(self, other_curr):
		return self.__add__(other_curr)

	def __rsub__(self, other_curr):
		return self.__sub__(other_curr)

	def __gt__(self, other_curr):
		if type(other_curr) == int or type(other_curr) == float:
			return self.amount > other_curr
		return self.amount > other_curr.convert_to(self.currency_type).amount


# This main is incomplete because not all methods are tested
# Some outputs are given by the comments next to the commands. Your code should be able to output these.
curr = Currency(7.50, 'USD')
print(curr) # 7.50 USD
curr2 = Currency(2, 'EUR')
print(curr2)  # 2.00 EUR
new_curr = curr2.convert_to(curr.currency_type) # 2.000000 EUR => 2.211600 USD
print(new_curr) # 2.21 USD
sum_curr = curr + curr2 # 2.000000 EUR => 2.211600 USD
print(sum_curr) # 9.71 USD
sum_curr2 = curr + 5.5
print(sum_curr2) # 13.00 USD
sub_curr = sum_curr2 - sum_curr
print(sub_curr) # 3.30 USD
print(curr > curr2) # True
print(curr > 10) # False