# -*- coding: utf8 -*-

import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King': 13, 'Ace':14}




def user_input_bool():
    '''
    Takes Y or N - whether the player wants to play again
    '''
    choice ='WRONG'
        
    while choice.upper() != 'N' and choice.upper() != 'Y':
        
        
        choice = input("Play one more time? enter (Y/N): ")
        
        if choice.upper() != 'N' and choice.upper() != 'Y':
            print("Please enter Y or N")
            
        if choice.upper() == 'N':
            return False
        elif choice.upper() == 'Y':
            return True





class Card:
    '''
    A single card with known suit and rank. The predefined constant values dictionary
    serves for ranking the cards according to their "numeric" value 
    '''
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = VALUES[rank]


    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    '''
    A complete deck comprising 52 unique cards generated based on the predefined constant tuples
    Always the same when created, therefore takes no parameters at "init"
    Has "shuffle" and "deal one" methods
    '''
    def __init__(self):

        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                #create the card object
                created_card = Card(rank,suit)
                self.all_cards.append(created_card)


    def shuffle(self):
        #shuffling the deck in-place
        random.shuffle(self.all_cards)
        print('Deck shuffled')


    def deal_one(self):
        #pops and returns a Card object from the deck (pops the last one) 
        return self.all_cards.pop()




class Player:
    '''
    Holds the player's hand (as a list of Card objects)
    Has methods to "play one" and "add cards"
    '''
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_one(self):
        #pops and returns a Card object from the hand (0 index) - taken cards will be added at the end of the list
        return self.hand.pop(0)


    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            #when list of multiple Card objects
            self.hand.extend(new_cards)
        else:
            #when a single Card object
            self.hand.append(new_cards)



    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'




if __name__ == '__main__':
    
    
    game_on = True

    #loop with the entire program (potentially multiple games)
    while game_on == True:

        victory = False
        #war = False

        new_deck = Deck()
        new_deck.shuffle()

        #a list to store what is currently "on table"
        on_table = []

        #counters of plays (card rank comparisons) and wars - used in game info given at the end
        play_counter = 0
        war_counter = 0

        #players are created here with generic names A and B 
        player_A = Player("A")
        player_B = Player("B")

        #dealing the entire deck into two hands
        for x in range(26):
            player_A.add_cards(new_deck.deal_one())
            player_B.add_cards(new_deck.deal_one())


        print('\n')
        print(player_A)
        print(player_B)
        print('\n')



        while victory == False:

            #chek if anybody has won
            if len(player_A.hand) == 0:
                print('Player A out of cards')
                victory = True
                winner = player_B.name
                break
            elif len(player_B.hand) == 0:
                print('Player B out of cards')
                victory = True
                winner = player_A.name
                break
            else:
                victory = False


            #playing and comparing cards
            play_counter += 1
            card_A = player_A.play_one()
            card_B = player_B.play_one()
            print(f'{play_counter}: {card_A} vs {card_B}    // a:{len(player_A.hand)},b:{len(player_B.hand)} ')
            

            on_table.append(card_A)
            on_table.append(card_B)

            if card_A.value > card_B.value:
                #cards from the table are shuffled before being added to a player's hand, otherwise an infinite game would be possible!
                random.shuffle(on_table)
                player_A.add_cards(on_table)
                print(f'\t {player_A.name} takes {len(on_table)} cards')
                on_table.clear()
            elif card_A.value < card_B.value:
                #cards from the table are shuffled before being added to a player's hand, otherwise an infinite game would be possible!
                random.shuffle(on_table)
                player_B.add_cards(on_table)
                print(f'\t {player_B.name} takes {len(on_table)} cards')
                on_table.clear()
            elif card_A.value == card_B.value:
                print('WAR! Each player plays a card face-down')
                war_counter += 1
                #exception handling used to check whether a player ran out of cards during the war (popping from an empty hand = index error)
                try:
                    card_C = player_A.play_one()
                    on_table.append(card_C)
                except IndexError:
                    print('HAND EMPTY DURING WAR')
                    victory = True
                    winner = player_B.name
                    break

                #exception handling used to check whether a player ran out of cards during the war (popping from an empty hand = index error)
                try:
                    card_D = player_B.play_one()
                    on_table.append(card_D)
                except IndexError:
                    print('HAND EMPTY DURING WAR')
                    victory = True
                    winner = player_A.name
                    break

                #if both players managed to play face-down cards in a war, the "on_table" list is NOT cleared and we go back to another basic card play & comparison


        #if the above while loop has ended, somebody has won
        print (f'GAME OVER! Winner: {winner}, number of comparisons: {play_counter}, number of wars: {war_counter}!')

        #Player's decision may result in another game or end the main while loop and terminate the program
        game_on = user_input_bool()


    print ('--- end of program ---')











