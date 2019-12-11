#Lab Test 24/10/19
#C18477502

def make_new_row(old_row):
	if old_row == []: #first row if needed
		return [1]
	new_row = [1] #start off with a 1
	for i in range(len(old_row)-1):
		new_row.append(old_row[i] + old_row[i+1]) #append the sum of the two digits above
	new_row.append(1) #end with a 1
	return new_row

def make_triangle(height,row=[1],triangle = []): #include default parameters for when only height is specified
	triangle.append(row) #first row
	if height > 1: #stop recursion once you've reached the bottom
		make_triangle(height-1,make_new_row(row),triangle) #call the function again but with less size and a new row
	return(triangle)

def print_triangle(triangle):
	for row in triangle:
		print(" ".join([str(i) for i in row]).center(len(triangle)*5)) #convert each row into a centered string with spaces

height = input("Enter the desired height of Pascal's triangle: ")

while 1:
	try:
		height = int(height) #try to convert to int
	except:
		height = input("Invalid input, please try again: ") #prompt for input again
	else:
		if height > 0:
			break #break once you have a valid positive int
		height = input("No negative numbers or zero please, try again: ")

triangle = (make_triangle(height))

print("Printing whole list of lists:")
print(triangle)

print("Printing lists with formatting:")
print_triangle(triangle)
