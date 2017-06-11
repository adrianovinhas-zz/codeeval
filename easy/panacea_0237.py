import sys

def parse_input_args(input_file):
	with open(input_file,'r') as f:
		return map(lambda line: map(lambda components: components.split(" "), 
									line.replace('\n','').split(" | ")),
				   f.readlines())

def main(input_file):
	for c in parse_input_args(input_file):
		print(sum(map(lambda x: int(x,16), c[0])) <= sum(map(lambda x: int(x,2), c[1])))

if __name__ == '__main__':
	main(sys.argv[1])