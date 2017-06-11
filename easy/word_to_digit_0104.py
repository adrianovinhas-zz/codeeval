import sys

numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(";"), f.readlines())

def translate_into_number(extended_number):
	return str(numbers.index(extended_number))

def main(input):
	for case in parse_file_info(input):
		print(''.join(map(lambda x: translate_into_number(x),case)))

if __name__ == '__main__':
	main(sys.argv[1])