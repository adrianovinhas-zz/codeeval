import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n',''), f.readlines())

def main(input):
	for case in parse_file_info(input):
		final_string = case[0]
		previous = case[0]
		for i in range(1,len(case)):
			if case[i] != previous:
				final_string += case[i]
			previous = case[i]
		print(final_string)

if __name__ == '__main__':
	main(sys.argv[1])