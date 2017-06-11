import sys

CARDS = ['J','Q','K','A']

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: list(map(lambda x: x.split(" "),
										 line.replace('\n','').split(" | "))), 
				   f.readlines())

def get_card_value(card,trump):
	trump_multiplier = 10 if trump == card[-1] else 1
	try:
		return int(card[:-1])*trump_multiplier	
	except:
		return (CARDS.index(card[:-1])+11)*trump_multiplier

def compare(card1, card2, trump):
	card1_value = get_card_value(card1,trump)
	card2_value = get_card_value(card2,trump)
	if card1_value > card2_value:
		return card1
	elif card2_value > card1_value:
		return card2
	else:
		return card1 + " " + card2

def main(input):
	for case in parse_file_info(input):
		print(compare(case[0][0], case[0][1], case[1][0]))

if __name__ == '__main__':
	main(sys.argv[1])