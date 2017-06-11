import sys
import math

def parse_file_info(filename):
	with open(filename,'r') as f:
		params = map(lambda line: list(map(lambda pair: tuple(pair.split(": ")), line.replace('\n','').split(", "))), f.readlines())
		return map(lambda single: {k: int(v) for k,v in single}, params)

def candy_assignment(costume):
	if costume == "Vampires":
		return 3
	elif costume == "Zombies":
		return 4
	else:
		return 5

def socialist_halloween(candies_per_costume, houses):
	return math.floor(sum(map(lambda cst: candy_assignment(cst[0])*cst[1]*houses,candies_per_costume.items()))/sum(candies_per_costume.values()))

def main(input):
	for case in parse_file_info(input):
		n_houses = case.pop('Houses')
		print(int(socialist_halloween(case,n_houses)))

if __name__ == '__main__':
	main(sys.argv[1])