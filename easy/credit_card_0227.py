import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').replace(' ',''), f.readlines())

def main(input):
	for case in parse_file_info(input):
		card_sum = sum(map(lambda x: 2*int(x),case[::2])) + sum(map(lambda x: int(x),case[1::2]))
		if card_sum%10 == 0:
			print("Real")
		else:
			print("Fake")

if __name__ == '__main__':
	main(sys.argv[1])