dec = int(input("Please enter a positive number in decimal: "))

if (dec < 1): #check to see if it's positive and not zero
    print("That number is not allowed")
else:
    div = 1
    bin = '' #empty string to start
    while (dec > div * 2):
        div = div * 2 #keep increasing the divisor until it's the biggest that'll fit in the number
    while (div >= 1):
        if (div <= dec):
            bin = bin + '1' #1 if it goes in
            dec = dec - div
        else:
            bin = bin + '0' #0 if it doesn't go in
        div = div / 2
    print(bin)
