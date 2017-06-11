import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: list(map(lambda elem: elem.split(" "), line.replace('\n','').split(" | "))), f.readlines())

def black_card(pirates, number):
	del pirates[number%len(pirates)]
	return pirates[0] if len(pirates)==1 else black_card(pirates, number) 

def main(input):
	for case in parse_file_info(input):
		print(black_card(case[0],int(case[1][0])-1))

if __name__ == '__main__':
	main(sys.argv[1])