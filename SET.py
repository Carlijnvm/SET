import random
import pygame
import time
import sys
import os

class Card:
    def __init__(self, symbol, number, color, shading):
        self.symbol = symbol
        self.number = number
        self.color = color
        self.shading = shading

    def __str__(self):
        return '%s%s%s%s' % (Card.colors[self.color], 
                             Card.symbols[self.symbol], 
                             Card.shadings[self.shading], 
                             Card.numbers[self.number])

    symbols = ["diamond", "squiggle", "oval"]
    numbers = ["1", "2", "3"]
    colors = ["red", "green", "purple"]
    shadings = ["filled", "shaded", "empty"]

class Deck:
    def __init__(self):
        self.cards = []
        for symbols in range(3):
            for numbers in range(3):
                for colors in range(3):
                    for shadings in range(3):
                        card = Card(colors, symbols, shadings, numbers)
                        self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    
    def pop_card(self):
        if len(self.cards) == 0:  
            print("Deck is empty. Reshuffling the deck.")
            self.shuffle()  #Reshuffle deck if empty
        return self.cards.pop()  

    
    def add_card(self, card):
        self.cards.append(card)
    
    def starting_cards(self):
        self.shuffle()
        table = []
        for i in range(12):
            table.append(self.pop_card()) 
        return table
#return '\n'.join(table) (is dit nog nodig?)

class Button():
    def __init__(self, x, y, image, card): 
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y) 
        self.clicked = False 
        self.card = card

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
    

#functies vergelijken kaarten en vinden sets
def check_if_set(card1, card2, card3):
    symbol_check = same_or_diff(card1.symbol, card2.symbol, card3.symbol)
    number_check = same_or_diff(card1.number, card2.number, card3.number)
    color_check = same_or_diff(card1.color, card2.color, card3.color)
    shading_check = same_or_diff(card1.shading, card2.shading, card3.shading)
    return symbol_check and number_check and color_check and shading_check

def same_or_diff(feature1, feature2, feature3):
    if feature1 == feature2 and feature2 == feature3:
        return True
    elif (feature1 != feature2) and (feature2 != feature3) and (feature1 != feature3):
        return True
    else:
        return False
    
def check_selected_set(clicked_cards, deck):
    if len(clicked_cards) == 3:
        card1, card2, card3 = clicked_cards
        if check_if_set(card1, card2, card3):
            print("This is a valid set!")
            #vervangen van de drie kaarten van de gevonden set
            
            #for card in [card1, card2, card3]:
                #deck.add_card(card)  #belangrijk dat ze teruggestopt worden, anders is het deck ineens leeg
            
            new_cards = []
            for _ in range(3):
                new_cards.append(deck.pop_card())
                
            return new_cards
        else:
            print("This is not a valid set.")
        clicked_cards.clear()
    return None
        
def find_all_sets(example_cards1):
    sets = []
    for i in range(len(example_cards1)):
        for j in range(i + 1, len(example_cards1)):
            for k in range(j + 1, len(example_cards1)):
                card1 = example_cards1[i]
                card2 = example_cards1[j]
                card3 = example_cards1[k]
                if check_if_set(card1, card2, card3):
                    sets.append((card1, card2, card3))  #dubbele haakjes, zodat het 1 argument is
    return sets

def find_one_set (example_cards2):
    set = []
    for i in range(len(example_cards2)):
        for j in range(i + 1, len(example_cards2)):
            for k in range(j + 1, len(example_cards2)):
                cardone = example_cards2[i]
                cardtwo = example_cards2[j]
                cardthree = example_cards2[k]
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



pygame.init()

pygame.font.init()
score = 0
score_increment = 1
font = pygame.font.Font(None, 48)

deck = Deck()
cards_on_table = deck.starting_cards()
screen = pygame.display.set_mode([610, 830])
pygame.display.set_caption('SET')




#12 random starting cards
image1 = pygame.image.load(str(cards_on_table[0]) + '.jpeg')
image2 = pygame.image.load(str(cards_on_table[1]) + '.jpeg')
image3 = pygame.image.load(str(cards_on_table[2]) + '.jpeg')
image4 = pygame.image.load(str(cards_on_table[3]) + '.jpeg')
image5 = pygame.image.load(str(cards_on_table[4]) + '.jpeg')
image6 = pygame.image.load(str(cards_on_table[5]) + '.jpeg')
image7 = pygame.image.load(str(cards_on_table[6]) + '.jpeg')
image8 = pygame.image.load(str(cards_on_table[7]) + '.jpeg')
image9 = pygame.image.load(str(cards_on_table[8]) + '.jpeg')
image10 = pygame.image.load(str(cards_on_table[9]) + '.jpeg')
image11 = pygame.image.load(str(cards_on_table[10]) + '.jpeg')
image12 = pygame.image.load(str(cards_on_table[11]) + '.jpeg')

#create button instances
card1_button = Button(30, 100, image1, cards_on_table[0])  
card2_button = Button(180, 100, image2, cards_on_table[1])  
card3_button = Button(330, 100, image3, cards_on_table[2]) 
card4_button = Button(480, 100, image4, cards_on_table[3]) 
card5_button = Button(30, 350, image5, cards_on_table[4])  
card6_button = Button(180, 350, image6, cards_on_table[5])  
card7_button = Button(330, 350, image7, cards_on_table[6])  
card8_button = Button(480, 350, image8, cards_on_table[7])  
card9_button = Button(30, 600, image9, cards_on_table[8]) 
card10_button = Button(180, 600, image10, cards_on_table[9])  
card11_button = Button(330, 600, image11, cards_on_table[10])  
card12_button = Button(480, 600, image12, cards_on_table[11])

button_list = [
    card1_button, card2_button, card3_button, card4_button,
    card5_button, card6_button, card7_button, card8_button,
    card9_button, card10_button, card11_button, card12_button
]

last_reset_time = time.time()

clicked_cards = []  

running = True
while running:
    screen.fill((153, 204, 255)) 

    score_text = font.render(f'Score: {score}', True, (0, 80, 255))
    screen.blit(score_text, (30, 30))

    if time.time() - last_reset_time >= 20:

        cards_on_table = deck.starting_cards()
        #Update the images for the new cards
        image1 = pygame.image.load(str(cards_on_table[0]) + '.jpeg')
        image2 = pygame.image.load(str(cards_on_table[1]) + '.jpeg')
        image3 = pygame.image.load(str(cards_on_table[2]) + '.jpeg')
        image4 = pygame.image.load(str(cards_on_table[3]) + '.jpeg')
        image5 = pygame.image.load(str(cards_on_table[4]) + '.jpeg')
        image6 = pygame.image.load(str(cards_on_table[5]) + '.jpeg')
        image7 = pygame.image.load(str(cards_on_table[6]) + '.jpeg')
        image8 = pygame.image.load(str(cards_on_table[7]) + '.jpeg')
        image9 = pygame.image.load(str(cards_on_table[8]) + '.jpeg')
        image10 = pygame.image.load(str(cards_on_table[9]) + '.jpeg')
        image11 = pygame.image.load(str(cards_on_table[10]) + '.jpeg')
        image12 = pygame.image.load(str(cards_on_table[11]) + '.jpeg')

        #Update the buttons for the new cards
        card1_button = Button(30, 100, image1, cards_on_table[0])
        card2_button = Button(180, 100, image2, cards_on_table[1])
        card3_button = Button(330, 100, image3, cards_on_table[2])
        card4_button = Button(480, 100, image4, cards_on_table[3])
        card5_button = Button(30, 350, image5, cards_on_table[4])
        card6_button = Button(180, 350, image6, cards_on_table[5])
        card7_button = Button(330, 350, image7, cards_on_table[6])
        card8_button = Button(480, 350, image8, cards_on_table[7])
        card9_button = Button(30, 600, image9, cards_on_table[8])
        card10_button = Button(180, 600, image10, cards_on_table[9])
        card11_button = Button(330, 600, image11, cards_on_table[10])
        card12_button = Button(480, 600, image12, cards_on_table[11])

        #Update the button list
        button_list = [
            card1_button, card2_button, card3_button, card4_button,
            card5_button, card6_button, card7_button, card8_button,
            card9_button, card10_button, card11_button, card12_button
        ]

        #Reset the timer
        last_reset_time = time.time()

    #
    for button in button_list:
        if button.draw():
            clicked_cards.append(button.card)  #
            if len(clicked_cards) == 3:  
                new_cards = check_selected_set(clicked_cards, deck)
                if new_cards:
                    score += score_increment
                    cards_on_table = [card for card in cards_on_table if card not in clicked_cards] + new_cards 
                    clicked_cards.clear()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.flip()  

pygame.quit()

