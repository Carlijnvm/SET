import random
import pygame
#import image

class Card:
    def __init__(self,symbol,number,color,shading):
        self.symbol=symbol
        self.number=number
        self.color=color
        self.shading=shading

    def __str__(self):
        return '%s, %s, %s, %s' % (Card.colors[self.color],
                           Card.symbols[self.symbol],
                           Card.shadings[self.shading],
                           Card.numbers[self.number])
    
    

    symbols=["diamond","squiggle","oval",]
    numbers=["1","2","3"]
    colors=["red","green","purple"]
    shadings=["filled","shaded","empty"]

class Deck:
    def __init__(self):
        self.cards = []
        for symbols in range(3):
            for numbers in range(3):
                for colors in range(3):
                    for shadings in range(3):
                        card=Card(colors,symbols,shadings,numbers)
                        self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self): #haalt onderste kaart van de stapel
        return self.cards.pop()
    
    def add_card(self, card): #misschien helemaal niet nodig
        self.cards.append(card)
    
    def starting_cards(self): #geeft 12 willekeurige startkaarten
        self.shuffle()
        table =[]
        for i in range(12):
            table.append(str(self.pop_card()))
        return table
#return '\n'.join(table)
    
#functies vergelijken kaarten en vinden sets
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

def find_all_sets(cards):
    sets = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                card1 = cards[i]
                card2 = cards[j]
                card3 = cards[k]
                if check_if_set(card1, card2, card3):
                    sets.append((card1, card2, card3))  #dubbele haakjes, zodat het 1 argument is
    return sets

def find_one_set (cards2):
    set = []
    for i in range(len(cards2)):
        for j in range(i + 1, len(cards2)):
            for k in range(j + 1, len(cards2)):
                cardone = cards2[i]
                cardtwo = cards2[j]
                cardthree = cards2[k]
                if check_if_set(cardone, cardtwo, cardthree):
                    set.append((cardone,cardtwo,cardthree))  
                    break
            else: 
                 continue
            break
        else:
             continue
        break            
    return set

#voorbeelden
card1 = Card(0,2,0,0)
card2 = Card(1,0,1,1)
card3 = Card(2,1,2,2)
#print(check_if_set(card1, card2, card3))  

card4 = Card(2,2,0,0)
card5 = Card(2,2,0,0)
card6 = Card(2,2,0,1)
#print(check_if_set(card4, card5, card6))  

#voorbeelden
cards = [
    Card(0, 0, 0, 0), Card(1, 0, 1, 1), Card(2, 1, 2, 2),
    Card(0, 1, 0, 1), Card(1, 2, 1, 2), Card(2, 0, 2, 0),
    Card(0, 2, 0, 2), Card(1, 1, 1, 0), Card(2, 2, 2, 1),
    Card(0, 1, 2, 0), Card(1, 0, 1, 2), Card(2, 2, 1, 1)
]

cards2 = [
    Card(1, 2, 0, 0), Card(1, 0, 2, 1), Card(1, 1, 1, 2),
    Card(0, 2, 1, 0), Card(1, 2, 2, 2), Card(2, 0, 2, 0),
    Card(0, 0, 0, 2), Card(2, 1, 0, 0), Card(2, 2, 2, 1),
    Card(0, 1, 2, 1), Card(0, 0, 1, 2), Card(2, 2, 1, 1)
]

#valid_sets = find_all_sets(cards)
#for card_set in valid_sets:
  #print([str(card) for card in card_set])

#valid_set = find_one_set(cards)
#for card_set in valid_set:
    #print([str(card) for card in card_set])

pygame.init()
#voorbeeld startkaarten printen
deck = Deck()
beginkaarten = deck.starting_cards()
#print(beginkaarten)
#beginkaarten_str = str(beginkaarten).replace(", ", '')
for i in range(12):
    beginkaarten[i] = str(beginkaarten[i]).replace(", ", '')
print(beginkaarten)

#for i in range(12):
    #beginkaarten_str[i]= beginkaarten_str[i] + '.jpeg'
#print((beginkaarten_str))


screen = pygame.display.set_mode([610, 830])
image1 = pygame.image.load(str(beginkaarten[0])+'.jpeg')
image2 = pygame.image.load(str(beginkaarten[1])+'.jpeg')
image3 = pygame.image.load(str(beginkaarten[2])+'.jpeg')
image4 = pygame.image.load(str(beginkaarten[3])+'.jpeg')
image5 = pygame.image.load(str(beginkaarten[4])+'.jpeg')
image6 = pygame.image.load(str(beginkaarten[5])+'.jpeg')
image7 = pygame.image.load(str(beginkaarten[6])+'.jpeg')
image8 = pygame.image.load(str(beginkaarten[7])+'.jpeg')
image9 = pygame.image.load(str(beginkaarten[8])+'.jpeg')
image10 = pygame.image.load(str(beginkaarten[9])+'.jpeg')
image11 = pygame.image.load(str(beginkaarten[10])+'.jpeg')
image12 = pygame.image.load(str(beginkaarten[11])+'.jpeg')
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #achtergrondkleur
    screen.fill((153, 204, 255))

    screen.blit(image1,(30,100))
    screen.blit(image2,(30,350))
    screen.blit(image3,(30,600))
    screen.blit(image4,(180,100))
    screen.blit(image5,(180,350))
    screen.blit(image6,(180,600))
    screen.blit(image7,(330,100))
    screen.blit(image8,(330,350))
    screen.blit(image9,(330,600))
    screen.blit(image10,(480,100))
    screen.blit(image11,(480,350))
    screen.blit(image12,(480,600))
 
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

