#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
	"""Display a standard user greeting."""
	print("hello_" + user_name.upper() + "!") 
hello_name('kleerene')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100
#and returns nothing.
def first_odds():
	"""Display all odd numbers in a given range."""
	for number in range(1,101):
		if number % 2 != 0:
			print(number)
first_odds()

#Question 3
#Write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
	"""Display the largest number in a list."""
	largest_number = max()
	return largest_number
a_list = [1, 2, 3, 4, 5, 6]
print(max(a_list))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4,
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean
#Type (true/false).
def is_leap_year(a_year):
	"""Determine whether a year entered is a leap year."""
	year = int(a_year)
	if year % 4 == 0 and year % 100 != 0:
		print(True)
	elif year % 400 == 0:
		print(True)
	elif year % 100 == 0:
		print(False)
	else:
		print(False)
is_leap_year(1946)

#Question 5
#Write a function to check to see if all numbers in a list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive
#numbers. The return should be boolean Type.
def is_consecutive(a_list):
	"""Determine whether a given list is consecutive or not consecutive."""

