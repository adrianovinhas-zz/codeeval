import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: map(lambda artist: map(int,artist.split(" ")),line.replace('\n','').split(" | ")), f.readlines())

def highest(scores):
	return [] if(len(scores[0]) == 0) else [reduce(lambda x,y: x if x>y else y, map(lambda l: l.pop(0),scores))] + highest(scores)

def main(input):
	for case in parse_file_info(input):
		print(' '.join(map(str,highest(case))))

if __name__ == '__main__':
	main(sys.argv[1])