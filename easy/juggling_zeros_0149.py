import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		actions = case[::2]
		bits = case[1::2]
		print(int(''.join(list(map(lambda x: len(x[1])*'1' if x[0] == "00" else x[1] ,zip(actions,bits)))),2))

if __name__ == '__main__':
	main(sys.argv[1])