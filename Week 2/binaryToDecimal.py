bin = input("Please enter a number in binary: ")

length = len(bin) - 1
i = 0
dec = 0
while (i <= length):
	dec += int(bin[i]) * 2 ** (length - i) #multiplying by int(bin[i]) makes it so nothing will happen for a zero
	i = i + 1
print(dec)
