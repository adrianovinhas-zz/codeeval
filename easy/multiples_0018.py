import sys
from itertools import dropwhile

def parse_input_args(input_file):
	with open(input_file,'r') as f:
		return map(lambda line: line.replace('\n','').split(','), f.readlines())

def main(input_file):
	values = parse_input_args(input_file)
	for v in values:
		print(multiples(int(v[0]),int(v[1])))

def stream_creator(n):
	multiplier = 0
	while(True):
		yield n * multiplier
		multiplier += 1

def multiples(x,n):
	return dropwhile(lambda number: number<x, stream_creator(n)).next()


if __name__ == '__main__':
	main(sys.argv[1])