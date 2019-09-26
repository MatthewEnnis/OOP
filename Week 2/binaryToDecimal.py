bin = input("Please enter a number in binary: ")

length = len(bin) - 1
i = 0
dec = 0
while (i <= length):
    dec = dec + int(bin[i]) * 2 ** (length - i)
    i = i + 1
print(dec)