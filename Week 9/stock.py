def get_data_list(file_name):
	data_file = open(file_name,"r")
	data_list = []
	for line_str in data_file:
		data_list.append(line_str.strip().split(","))
	data_list.pop(0)
	return data_list

def get_monthly_averages(data_list):
	monthlyavgs = []
	avgtop,avgbottom = 0,0
	currentmonth = data_list[0][0][:-3]
	for line in data_list:
		if line[0][:-3] == currentmonth:
			avgtop += int(line[5]) * float(line[6])
			avgbottom += int(line[5])
		else:
			monthlyavgs.append(((avgtop/avgbottom),currentmonth))
			currentmonth = line[0][:-3]
			avgtop = int(line[5]) * float(line[6])
			avgbottom = int(line[5])
	monthlyavgs.append(((avgtop/avgbottom),currentmonth))
	return monthlyavgs

def print_info(monthly_averages_list):
	monthdict = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
	print("Best 6 Months:")
	monthly_averages_list.sort(reverse=True)
	for avgtuple in monthly_averages_list[:6]:
		print("{0} {1}: {2:.2f}".format(monthdict[int(avgtuple[1][-2:])],avgtuple[1][:4],avgtuple[0]))
	print("\nWorst 6 Months:")
	monthly_averages_list.sort()
	for avgtuple in monthly_averages_list[:6]:
		print("{0} {1}: {2:.2f}".format(monthdict[int(avgtuple[1][-2:])],avgtuple[1][:4],avgtuple[0]))

def main():
	data_list = get_data_list("goog.csv")
	monthly_averages = get_monthly_averages(data_list)
	print_info(monthly_averages)

main()