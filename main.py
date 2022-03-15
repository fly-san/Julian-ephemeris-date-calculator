def is_leap_year(year):
	# Skip if not divisible by 4
	if year % 4 != 0:
		return False

	# In 1582 there was a convention that decided:
	# Fourth years that fell on century changes were omitted as leap years unless they were a four hundredth year

	# If year greater than 1582, then skip if century change but not divisible by 400
	if year > 1582 and year % 100 == 0 and year % 400 != 0:
		return False

	# Anything left should be a leap year
	return True

lookup = [1, 3, 5, 7, 8, 10, 12]
def handle_months(year, month):
	result = 0
	
	for i in range(1, month):	
		if i in lookup:		
			result += 31
		elif i == 2:
			if is_leap_year(year): 	
				result += 29
			else:				
				result += 28
		else:	
			result += 30

	return result

def compute_extra_days(year, month, day, hours, minutes, seconds):
	month = month or int(input("Wanted month in MM format: "))
	day = day or int(input("Wanted day in DD format: "))
	 
	# Add days + days in months
	days = day + handle_months(year, month)

	if year > 0 and year < 1582:
		days -= 1


	if not (hours or minutes or seconds):
		# Request for HH:MM:SS
		date_time = input("Time in hh:mm:ss format: ").split(":")
		hours = int(date_time[0])
		minutes = int(date_time[1])
		seconds = int(date_time[2])	

	minutes = (hours * 60) + minutes
	seconds = (minutes * 60) + seconds

	seconds_in_days = seconds / 86400
	extra_days = seconds_in_days + days

	return extra_days

def compute_days(year = None, month=  None, day = None, hours = None, minutes = None, seconds = None ):	
	year = year or int(input("Wanted year in (+/-) YYYY format: "))

	# Get the difference between target year and 4713 BCE
	years = -4713 - year

	# Add +1 to years after the year 0 to account for the year 0 itself
	# (Ex: difference between years 1BC and 1AD is 3)
	if year > 0:
		years += 1

	leap_years = compute_leap_years(years, year)
	normal_years = abs(years) - abs(leap_years)

	days_in_leap_years = abs(leap_years * 366)
	days_in_normal_years = abs(normal_years * 365)

	extra_days = compute_extra_days(year, month, day, hours, minutes, seconds)

	return days_in_normal_years + days_in_leap_years - 0.5 + extra_days 


def compute_leap_years(years, year):
	# Initialize leap years counter
	leap_years = 0

	start = years
	target = 0

	if year > 0:	
		target = -years - 4713 
		start = -4713

	for i in range(start, target):
		if is_leap_year(i):			
			leap_years += 1
		else:
			continue

	if year > 1582:
		leap_years -= 11

	return leap_years

if __name__ == "__main__":
	result = compute_days(2003,3,17,22,47,00)
	print(result)
