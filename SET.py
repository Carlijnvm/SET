from random import shuffle, sample #we only need those two
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
                             Card.numbers[self.number]) #

    symbols = ["diamond", "squiggle", "oval"]
    numbers = ["1", "2", "3"]
    colors = ["red", "green", "purple"]
    shadings = ["filled", "shaded", "empty"]

class Deck:
    def __init__(self):
        self.cards = []
        for symbol in range(3):
            for number in range(3):
                for color in range(3):
                    for shading in range(3):
                        card = Card(symbol, number, color, shading)  
                        self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

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

class Game: #added Game class, restructured code into Game class
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([610, 860])
        pygame.display.set_caption('SET')
        self.clock = pygame.time.Clock() #added for setting frame rate
        self.font = pygame.font.Font(None, 48)  

        #Initialize game
        #added many "self" things because its now part of the Game class
        self.deck = Deck()
        self.deck.shuffle()
        self.cards_on_table = self.deck.starting_cards()
        self.selected_indices = []  #added for storing clicked cards
        self.score = 0
        self.computer_score = 0 #added computer score as said in assignment
        self.last_set_found_time = time.time()
        self.timer_duration = 30  #changed form 20 to 30, was too fast:)


    def same_or_diff(feature1, feature2, feature3): #moved this function before def check if set
        if feature1 == feature2 and feature2 == feature3:
            return True
        elif (feature1 != feature2) and (feature2 != feature3) and (feature1 != feature3):
            return True
        else:
            return False

    #Functions to compare cards and find sets
    @staticmethod #to fix a bug in the number of argument, this worked somehow
    def check_if_set(card1, card2, card3):
        if not card1==card2==card3: #otherwise it will say that three cards that are the same are a set
            symbol_check = Game.same_or_diff(card1.symbol, card2.symbol, card3.symbol) #added Game. because the function is in the Gameclass, could also be self but not sure.
            number_check = Game.same_or_diff(card1.number, card2.number, card3.number)
            color_check = Game.same_or_diff(card1.color, card2.color, card3.color)
            shading_check = Game.same_or_diff(card1.shading, card2.shading, card3.shading)
            return symbol_check and number_check and color_check and shading_check
        else:
            return False

    def replace_cards(self, cards, indices, deck): #this function calles for some cards with indices to be replaced by new cards from the deck
        for index in indices: 
            if len(deck.cards) >= 3:
                cards[index] = deck.pop_card()

    def find_one_set(self, cards):
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                for k in range(j + 1, len(cards)):
                    if self.check_if_set(cards[i], cards[j], cards[k]):
                        return (i, j, k) #changed this because we only need to return the indices of the set. We next use this in line 153 (probably changes so around line 153)
        return None #much simpler than all the breaks and continues

    def handle_click(self, pos): #gave clicking the cards another shot, reused some code
        positions = [
            (30, 100), (180, 100), (330, 100), (480, 100),  
            (30, 350), (180, 350), (330, 350), (480, 350),  
            (30, 600), (180, 600), (330, 600), (480, 600)
        ]
        
        for i, (x, y) in enumerate(positions):
            if x <= pos[0] <= x + 100 and y <= pos[1] <= y + 200: 
                #if clicked between edges of card   
                #pos[0] is x-coordinate, pos[1] is y-coordinate  
                #100 and 200 are the card width and height
                if i in self.selected_indices: #self.selected_indices is a list keeping track of the indices of clicked cards
                    self.selected_indices.remove(i) #if card i is already selected, it will be deselected and removed from the list
                else:
                    self.selected_indices.append(i) #if card i is not selected, it will be selected
                
                #when three cards are selected, the set is validated/checked
                if len(self.selected_indices) == 3:
                    self.validate_set()

    def validate_set(self): #added this function to check if the selected cards are a set
        try:
            selected_cards = [self.cards_on_table[i] for i in self.selected_indices] #selected cards = cards on table with the indices of the selected cards
            if self.check_if_set(*selected_cards):
                print("That is a valid set:)")
                self.score += 1 #score updated for player
                self.replace_cards(self.cards_on_table, self.selected_indices, self.deck) 
                #Here we use def replace_cards(cards,indices,deck) to replace the cards that were part of the set found by the player
                self.last_set_found_time = time.time() #reset the timer
            else:
                print("Not a valid set,try again.") #if the selected cards are NOT a set
            self.selected_indices = [] #clear the list of indices of selected cards after checking a set (valid or not)
        except IndexError: #for when invalid index is accessed (this should not happen)
            self.selected_indices = [] #reset selection to prevent errors that could occur

    def run(self):
        running = True 
        while running:
            # Process events first
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False #if user closes window, game stops
                elif event.type == pygame.MOUSEBUTTONDOWN: #if mouse is clicked
                    self.handle_click(pygame.mouse.get_pos()) #handle the click with def handle_click()

            current_time = time.time() #gets current time for comparison in the next if statement
            if current_time - self.last_set_found_time >= self.timer_duration: #checks is more than 30 seconds have passed since last set was found
                #Computers turn
                set_indices = self.find_one_set(self.cards_on_table) #checks if a valid set is on screen #gets the indices of the found set
                if set_indices:
                    print("Computer found a SET! Replacing some cards...") #if a valid set is found by computer, it will print this and the computer gets a point
                    self.computer_score += 1
                    self.replace_cards(self.cards_on_table, set_indices, self.deck) #the cards from the set that was found by the computer are replaced
                    self.last_set_found_time = current_time #timer is reset
                else:
                    print("Time's up! Replacing some cards...") #it could be that no set was found by computer on the screen, so it will print this.
                    self.replace_cards(self.cards_on_table, sample(range(len(self.cards_on_table)), 3), self.deck) #3 random cards are replaced
                    self.last_set_found_time = current_time #timer is reset

            self.draw() #call the draw function to update the screen
            self.clock.tick(30)  #30 frames per second, make it smoother

        pygame.quit() #if game is not running, it will quit, this is outside the while running loop
        sys.exit()

    def draw(self):
        self.screen.fill((153, 204, 255)) #background color
        
        score_text = self.font.render(f'Player: {self.score}                         Computer: {self.computer_score}', True, (0, 80, 255)) 
        #the spaces between player and computer score are there to have the computer score on the top right of the screen
        self.screen.blit(score_text, (20, 20)) #gets player and computer score on screen
        
        
        positions = [
            (30, 100), (180, 100), (330, 100), (480, 100),  
            (30, 350), (180, 350), (330, 350), (480, 350),     #these are tuples in a list, each tuple is a card position
            (30, 600), (180, 600), (330, 600), (480, 600)
        ]
        
        for i, card in enumerate(self.cards_on_table): #enumerate is a function that adds an index to each element in the list
            x, y = positions[i] #gets the x,y-position from the list
            #HIGHLIGHTS SELECTED CARDS
            if i in self.selected_indices: #if the index of a card is in the list of selected indices
                pygame.draw.rect(self.screen, (255, 255, 0), (x-5, y-5, 110, 210), 5) #draws yellow rectangle around selected cards
            
            
            if card is not None:
                try:
                    image = pygame.image.load(f"images/{str(card)}.jpeg") #loads the image of the cards. I stored all images in a folder called images, it looks a bit more organized than 
                    #image = pygame.transform.scale(image, (100, 200))
                    self.screen.blit(image, (x, y))
                except FileNotFoundError: #if images cannot be loaded. this red error message will be displayed
                    error_message1 = "Make sure the card images are in" 
                    error_message2 = "the 'images' folder in your directory"      #i had to use multiple lines because the error message was too long and this fixed it
                    error_message3 = "with the right filenames."
                    text1 = self.font.render(error_message1, True, (255, 0, 0))
                    text2 = self.font.render(error_message2, True, (255, 0, 0))    #so i had to do everything three times
                    text3 = self.font.render(error_message3, True, (255, 0, 0))
                    self.screen.blit(text1, (40, 400))
                    self.screen.blit(text2, (25, 450))    #tweaked with the x,y-values to get the three lines in the right place
                    self.screen.blit(text3, (100, 500))
                    #this could probably be done in a better way, but it works
        pygame.display.flip()

if __name__ == "__main__": #checks if the python file is being run directly or imported
    game = Game() #this initializes the Game class, setting up everything needed for the game
    game.run() #this starts the game with the run function
