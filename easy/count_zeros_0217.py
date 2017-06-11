import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: tuple(map(int,line.replace('\n','').split(" "))), f.readlines())

def count_zeros(n_zeros, limit):		
	return filter(lambda string: len(list(filter(lambda x: x=='0',string)))==n_zeros, 
				  map(lambda x: bin(x)[2:], xrange(1,limit+1)))

def main(input):
	for case in parse_file_info(input):
		print(len(list(count_zeros(case[0],case[1]))))

if __name__ == '__main__':
	main(sys.argv[1])