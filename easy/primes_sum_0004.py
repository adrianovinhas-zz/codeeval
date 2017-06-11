import math

def is_prime(number):
	upper_bound = int(math.ceil(math.sqrt(number)))+1
	for i in xrange(2,upper_bound):
		if number%i == 0:
			return False
	return True

def main():
	n_primes = 1
	sum_primes = 2
	candidate_number = 3
	while n_primes < 1000:
		if is_prime(candidate_number) is True:
			n_primes += 1
			sum_primes += candidate_number
		candidate_number += 1
	print(sum_primes)


if __name__ == '__main__':
	main()