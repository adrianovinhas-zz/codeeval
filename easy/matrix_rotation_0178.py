import sys
import math

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		line_length = int(math.sqrt(len(case)))
		matrix = [case[i:i+line_length] for i in range(0,len(case),line_length)]
		final_matrix = [line[i] for i in range(line_length) for line in matrix[::-1]]
		print(' '.join(final_matrix))

if __name__ == '__main__':
	main(sys.argv[1])