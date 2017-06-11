import sys

def parse_input_args(input_file):
	with open(input_file,'r') as f:
		return map(lambda line: line.replace('\n','').split(' '), f.readlines())

def main(input_file):
	for v in parse_input_args(input_file):
		print(' '.join(list(fizz_buzz(int(v[0]),int(v[1]),int(v[2])))))

def replace(number,x,y):
	is_fizz = 'F' if number%x == 0 else ''
	is_buzz = 'B' if number%y == 0 else ''
	replacement = is_fizz + is_buzz
	if replacement == '':
		return str(number) 
	else:
		return replacement

def fizz_buzz(x,y,limit):
	return (replace(i,x,y) for i in xrange(1,limit+1))

if __name__ == '__main__':
	main(sys.argv[1])