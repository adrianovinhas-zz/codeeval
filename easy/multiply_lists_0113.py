import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: list(map(lambda x: x.split(" "),
										 line.replace('\n','').split(" | "))), 
				   f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(' '.join(list(map(lambda x: str(int(x[0])*int(x[1])), zip(case[0],case[1])))))
			
if __name__ == '__main__':
	main(sys.argv[1])