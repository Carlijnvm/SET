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
pygame.display.set_caption('SET')

#twelve random starting cards
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

#button class
class Button():
    def __init__(self, x, y, image): #x,y-coördinates for placement
        self.image = image
        self.rect = self.image.get_rect() #get rectangle from image
        self.rect.topleft = (x, y) #where we want the image
        self.clicked = False #starting value each button is not clicked

    def draw(self):
        action = False
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()
        
        #check mouse over buttons and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                #0 for leftmost button
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create button instances
card1_button = Button(30, 100, image1)
card2_button = Button(180, 100, image2)
card3_button = Button(330, 100, image3)
card4_button = Button(480, 100, image4)
card5_button = Button(30, 350, image5)
card6_button = Button(180, 350, image6)
card7_button = Button(330, 350, image7)
card8_button = Button(480, 350, image8)
card9_button = Button(30, 600, image9)
card10_button = Button(180, 600, image10)
card11_button = Button(330, 600, image11)
card12_button = Button(480, 600, image12)
#andere 10 nog toevoegen

running = True
while running:

    #achtergrondkleur
    screen.fill((153, 204, 255))
        
    if card1_button.draw():
        print('1')
    if card2_button.draw():
        print('2')
    if card3_button.draw():
        print('3')
    if card4_button.draw():
        print('4')
    if card5_button.draw():
        print('5')
    if card6_button.draw():
        print('6')
    if card7_button.draw():
        print('7')
    if card8_button.draw():
        print('8')
    if card9_button.draw():
        print('9')
    if card10_button.draw():
        print('10')
    if card11_button.draw():
        print('11')
    if card12_button.draw():
        print('12')

    #12 startkaarten
    #screen.blit(image1,(30,100))
    #screen.blit(image2,(180,100))
    #screen.blit(image3,(330,100))
    #screen.blit(image4,(480,100))
    #screen.blit(image5,(30,350))
    #screen.blit(image6,(180,350))
    #screen.blit(image7,(330,350))
    #screen.blit(image8,(480,350))
    #screen.blit(image9,(30,600))
    #screen.blit(image10,(180,600))
    #screen.blit(image11,(330,600))
    #screen.blit(image12,(480,600))

    #Did the user click the window close button?
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update() #updates game window at each iteration 
 
    # Flip the display
    #pygame.display.flip()

# Done! Time to quit.
pygame.quit()

