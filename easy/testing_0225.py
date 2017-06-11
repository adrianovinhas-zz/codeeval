import sys
from functools import reduce

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" | "), f.readlines())

def get_bug_status(n_bugs):
	if n_bugs == 0:
		return "Done"
	elif n_bugs <= 2:
		return "Low"
	elif n_bugs <= 4:
		return "Medium"
	elif n_bugs <= 6:
		return "High"
	else:
		return "Critical"

def main(input):
	for case in parse_file_info(input):
		list_of_possible_bugs = map(lambda test_vs_dsgn: reduce(lambda x,y: x==y,test_vs_dsgn), zip(case[0],case[1]))
		n_bugs = len(list(filter(lambda x: x==False, list_of_possible_bugs)))
		print(get_bug_status(n_bugs))

if __name__ == '__main__':
	main(sys.argv[1])