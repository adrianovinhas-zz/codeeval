import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: list(map(lambda x: x.split(" "),
										 line.replace('\n','').split(" | "))), 
				   f.readlines())

def football_fans(countries_fans_list):
	d = dict()
	for country,fans_list in enumerate(countries_fans_list):
		for f in fans_list:
			d[f] = [str(country+1)] if f not in d.keys() else d[f]+[str(country+1)]
	return d

def main(input):
	for case in parse_file_info(input):
		answer = football_fans(case)
		print(''.join(['%s:%s' % (key, ','.join(answer[key])+'; ') 
						for key in sorted(answer.keys(),key=lambda x: int(x))]))

if __name__ == '__main__':
	main(sys.argv[1])