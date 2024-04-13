from functools import lru_cache

FIVE_NAMES = ["Katie", "Jenny", "Samantha", "Sara", "Emily"]

AGES = [25, 30, 35, 40, 45]

MAP_NAME_TO_AGE = {name:age for name, age in zip(FIVE_NAMES, AGES)}

def average_age():
	return sum(AGES) / len(AGES)

def reverse_names():
	return [name[::-1] for name in FIVE_NAMES]

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)


# Following will run faster
@lru_cache(maxsize=None)
def fibonacci_memo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_memo(n-1) + fibonacci_memo(n-2)

# import webbrowser

# def open_webpage():
# 	webbrowser.open('https://www.google.com')

# open_webpage()

def test_average_age():
	assert average_age() == 35

def get_name_to_age():
	return MAP_NAME_TO_AGE;

def calculateDaysBetweenDates(begin,end):
	from datetime import datetime
	begin = datetime.strptime(begin, "%Y-%m-%d")
	end = datetime.strptime(end, "%Y-%m-%d")
	return abs((end - begin).days)