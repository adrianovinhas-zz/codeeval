import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n',''), f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(''.join(map(lambda x: x.upper() if x.islower() else x.lower(), case)))
			
if __name__ == '__main__':
	main(sys.argv[1])