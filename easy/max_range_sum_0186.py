import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(";"), f.readlines())

def max_range_sum(days, sequence):
	maximum = max([sum(sequence[i:i+days]) for i in range(0,len(sequence)-days+1)])
	return maximum if maximum > 0 else 0

def main(input):
	for case in parse_file_info(input):
		print(max_range_sum(int(case[0]),map(int,case[1].split(" "))))

if __name__ == '__main__':
	main(sys.argv[1])