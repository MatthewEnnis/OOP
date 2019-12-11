class Clock(object):
	def __init__(self,hours:int=0,minutes:int=0,seconds:int=0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds
	
	def check_time(self,time:str):
		"""Returns True if the string is correctly formatted (HH:MM:SS), returns False otherwise"""
		try:
			hours,minutes,seconds = [int(i) for i in time.split(":")]
			if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
				raise
		except:
			return False
		return True
	
	def change_time(self,time:str):
		"""Sets the clock time to the parameter if valid"""
		if self.check_time(time):
			self.__hours,self.__minutes,self.__seconds = [int(i) for i in time.split(":")]
	
	def __str__(self):
		return "{:02}:{:02}:{:02}".format(self.__hours,self.__minutes,self.__seconds)
	
	def add_time(self,time:str):
		"""Adds the time parameter to time if valid"""
		if self.check_time(time):
			addhours,addminutes,addseconds = [int(i) for i in time.split(":")]
			
			self.__seconds = self.__seconds + addseconds
			self.__minutes = self.__minutes + addminutes + self.__seconds // 60
			self.__hours = self.__hours + addhours + self.__minutes // 60
			
			self.__hours,self.__minutes,self.__seconds = self.__hours % 24,self.__minutes % 60,self.__seconds % 60
	
	def set_alarm(self,time:str):
		"""Sets the alarm to the time parameter"""
		if self.check_time(time):
			self.alarm = Clock()
			self.alarm.change_time(time)
			print("Alarm set for",self.alarm)
	
	def ring_alarm(self):
		"""Prints a song if the current time is the alarm time"""
		try:
			if [self.__hours,self.__minutes,self.__seconds] == [self.alarm.__hours,self.alarm.__minutes,self.alarm.__seconds]:
				print(u"\u266B","la la la",u"\u266B")
			else:
				print("It's not alarm time")
		except:
			print("Alarm hasn't been set")

clock1 = Clock(12,34,56)
print("Clock1 is",clock1)
clock1.set_alarm(input("Set alarm time: "))
clock1.change_time(input("Set current time: "))
clock1.ring_alarm()
