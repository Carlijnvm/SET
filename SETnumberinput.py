import random
import pygame
import time
import sys

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
        

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        if len(self.cards) <= 2:
            print("No cards left in deck. Game is finished!")
            pygame.quit()
            sys.exit()
        return self.cards.pop()

    def starting_cards(self):
        self.shuffle()
        table = []
        for i in range(12):
            table.append(self.pop_card()) 
        return table



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

pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 48)

#Initialize game
deck = Deck()
deck.shuffle()
cards_on_table = deck.starting_cards()
score = 0
last_reset_time = time.time()

#Setup screen
screen = pygame.display.set_mode([610, 860])
pygame.display.set_caption('SET')

def replace_cards(cards, indices, deck):
    for idx in indices:
        if len(deck.cards) >= 3:
            cards[idx] = deck.pop_card()
        


def draw_cards(cards):
    positions = [
        (30, 100), (180, 100), (330, 100), (480, 100),  
        (30, 350), (180, 350), (330, 350), (480, 350),  
        (30, 600), (180, 600), (330, 600), (480, 600),  
    ]

    for i, card in enumerate(cards):
        x, y = positions[i]
        if card is not None:
            try:
                #Load card image dynamically
                image = pygame.image.load(f"{str(card)}.jpeg")
                screen.blit(image, (x, y))
            except FileNotFoundError:
                #Draw placeholder rectangle if image is missing
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 200))
                pygame.draw.rect(screen, (0, 0, 0), (x, y, 100, 200), 2)

            #Draw card number below the card
            card_number = font.render(str(i + 1), True, (0, 0, 0))
            screen.blit(card_number, (x + 40, y + 210))  #Centered below the card
        else:
            pass 


running = True
while running:
    screen.fill((153, 204, 255))  #Light blue background

    #Draw score
    score_text = font.render(f'Score: {score}', True, (0, 80, 255))
    screen.blit(score_text, (20, 20))

    #Draw cards
    draw_cards(cards_on_table)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    #Terminal input for selecting cards
    if running:
        print("Enter three card numbers seperated by a space to select a SET (example: '1 2 3'): ")
        try:
            #Check if time to reset cards
            if time.time() - last_reset_time >= 20:
                print("Time's up! Resetting some cards...")
                replace_cards(cards_on_table, random.sample(range(len(cards_on_table)), 3), deck)
                last_reset_time = time.time()
            user_input = input()
            indices = [int(x) - 1 for x in user_input.split()]
            if len(indices) != 3:
                raise ValueError("You must select exactly 3 cards!")

            selected_cards = [cards_on_table[i] for i in indices]
            if check_if_set(*selected_cards):
                print("That is a valid set:)")
                score += 1
                replace_cards(cards_on_table, indices, deck)
                last_reset_time = time.time()
            else:
                print("Not a valid set,try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter 3 valid card numbers.")

pygame.quit()