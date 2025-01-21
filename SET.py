import random

class Card:
    def __init__(self,symbol,number,color,shading):
        self.symbol=symbol
        self.number=number
        self.color=color
        self.shading=shading

    def __str__(self):
        return '%s, %s, %s, %s' % (Card.symbols[self.symbol],
                           Card.numbers[self.number],
                           Card.colors[self.color],
                           Card.shadings[self.shading])

    symbols=["diamond","squiggle","oval",]
    numbers=["1","2","3"]
    colors=["red","green","purple"]
    shadings=["solid","striped","open"]

class Deck:
    def __init__(self):
        self.cards = []
        for symbols in range(3):
            for numbers in range(3):
                for colors in range(3):
                    for shadings in range(3):
                        card=Card(symbols,numbers,colors,shadings)
                        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)


    
def check_if_set(card1,card2,card3):
    symbol_check = all_same_or_all_diff(card1.symbol,card2.symbol,card3.symbol)
    number_check = all_same_or_all_diff(card1.number,card2.number,card3.number)
    color_check = all_same_or_all_diff(card1.color,card2.color,card3.color)
    shading_check = all_same_or_all_diff(card1.shading,card2.shading,card3.shading)
    return symbol_check and number_check and color_check and shading_check

def all_same_or_all_diff (feature1, feature2, feature3):
	if feature1 == feature2 and feature2 == feature3: #hiermee hebben we ook aangetoond dat feature1=feature3
		return True
	elif (feature1 != feature2) and (feature2 != feature3) and (feature1 != feature3):
		return True
	else:
		return False


#voorbeelden
card1 = Card(0,2,0,0)
card2 = Card(1,0,1,1)
card3 = Card(2,1,2,2)
print(check_if_set(card1, card2, card3))  


card4 = Card(2,2,0,0)
card5 = Card(2,2,0,0)
card6 = Card(2,2,0,1)
print(check_if_set(card4, card5, card6))  


def find_all_sets(cards):
    sets = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                card1 = cards[i]
                card2 = cards[j]
                card3 = cards[k]
                if check_if_set(card1, card2, card3):
                    sets.append((card1, card2, card3))  
    return sets

def find_one_set (cards2):
    for i in range(len(cards2)):
        for j in range(i + 1, len(cards2)):
            for k in range(j + 1, len(cards2)):
                cardone = cards[i]
                cardtwo = cards[j]
                cardthree = cards[k]
                if check_if_set(cardone, cardtwo, cardthree):
                    return (cardone,cardtwo,cardthree)


#voorbeelden
cards = [
    Card(0, 0, 0, 0), Card(1, 0, 1, 1), Card(2, 1, 2, 2),
    Card(0, 1, 0, 1), Card(1, 2, 1, 2), Card(2, 0, 2, 0),
    Card(0, 2, 0, 2), Card(1, 1, 1, 0), Card(2, 2, 2, 1),
    Card(0, 1, 2, 0), Card(1, 0, 1, 2), Card(2, 2, 1, 1)
]

cards2 = [
    Card(1, 2, 0, 0), Card(1, 0, 2, 1), Card(2, 1, 2, 2),
    Card(0, 2, 1, 0), Card(1, 2, 2, 2), Card(2, 0, 2, 0),
    Card(0, 0, 0, 2), Card(2, 1, 0, 0), Card(2, 2, 2, 1),
    Card(0, 1, 2, 1), Card(0, 0, 1, 2), Card(2, 2, 1, 1)
]

valid_sets = find_all_sets(cards)
for card_set in valid_sets:
   print([str(card) for card in card_set])

valid_set = find_one_set (cards2)

for card_set in valid_set:
    print([str(card) for card in card_set])



