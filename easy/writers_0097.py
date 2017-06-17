import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split("| "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		coded_author = map(int,case[1].split(" "))
		print(''.join([case[0][i-1] for i in coded_author]))
			
if __name__ == '__main__':
	main(sys.argv[1])