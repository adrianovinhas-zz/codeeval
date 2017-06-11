import math
from itertools import dropwhile

def is_palindrome(number):
	return number==number[::-1]

def is_prime(number):
	upper_bound = int(math.ceil(math.sqrt(number)))+1
	for i in xrange(2,upper_bound):
		if number%i == 0:
			return False
	return True

def main():
	print(dropwhile(lambda x: is_prime(x) is False or is_palindrome(str(x)) is False, xrange(1000,1,-1)).next())

if __name__ == '__main__':
	main()