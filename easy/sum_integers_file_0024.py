import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: int(line.replace('\n','')), f.readlines())

def main(input):
	print(sum(parse_file_info(input)))
			
if __name__ == '__main__':
	main(sys.argv[1])