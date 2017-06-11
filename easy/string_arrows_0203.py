import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: [line[i:i+5] for i in xrange(0,len(line))], f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(len(list(filter(lambda x: x=='<--<<' or x=='>>-->',case))))

if __name__ == '__main__':
	main(sys.argv[1])