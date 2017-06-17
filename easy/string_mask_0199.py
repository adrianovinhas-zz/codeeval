import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(''.join(list(map(lambda pair: pair[0] if pair[1]=='0' else pair[0].upper(),zip(case[0],case[1])))))

if __name__ == '__main__':
	main(sys.argv[1])