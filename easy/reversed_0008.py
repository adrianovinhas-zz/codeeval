import sys

def parse_input_args(input_file):
	with open(input_file,'r') as f:
		return filter(lambda line: line != '', map(lambda line: line.replace('\n','').split(' '), f.readlines()))

def main(input_file):
	for case in parse_input_args(input_file):
		print(' '.join(case[::-1]))

if __name__ == '__main__':
	main(sys.argv[1])