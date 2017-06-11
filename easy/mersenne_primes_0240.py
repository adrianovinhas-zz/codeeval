import math
import sys
from itertools import takewhile

def parse_input_args(input_file):
	with open(input_file,'r') as f:
		return map(lambda line: line.replace('\n',''), f.readlines())

def main(input_file):
	values = parse_input_args(input_file)
	for v in values:
		print(', '.join(list(mersenne(int(v)))))

def is_prime(number):
	upper_bound = int(math.ceil(math.sqrt(number)))+1
	for i in xrange(2,upper_bound):
		if number%i == 0:
			return False
	return True

def generate_natural_numbers():
	i = 1
	while 1:
		i += 1
		yield i

def mersenne(bound):
	prime_numbers = ifilter(lambda x: is_prime(x), generate_natural_numbers())
	#mersenne_candidates = map(lambda p: 2**p-1, generate_natural_numbers())
	return map(str, takewhile(lambda x: x<bound, filter(lambda x: is_prime(x), generate_natural_numbers())))

if __name__ == '__main__':
	main(sys.argv[1])