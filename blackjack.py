from abc import ABC, abstractclassmethod
import random
import numpy as np

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value 

class Deck:
    def __init__(self):
        self.shoe = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    @property
    def create_deck(self):
        for i in self.suits:
            for j in self.ranks:
                value = 0
                if j == "Jack" or j == "Queen" or j == "King":
                    value = 10
                elif j == "Ace":
                    value = 11
                else:
                    value = int(j)
                self.shoe.append(Card(suit = i, rank = j, value = value))

    def shuffle(self):
        random.shuffle(self.shoe)

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_total = 0

class Participator(ABC):
    def __init__(self, shoe):
        self.hand: Hand = Hand()
        self.ace_count = 0
        self.bust = False
        self.shoe = shoe

    @abstractclassmethod
    def starting_cards(self):
        ...
    
    @abstractclassmethod
    def calculate_value(self):
        ...
    
    @abstractclassmethod
    def hit(self):
        ...

class Player(Participator):
    def __init__(self, name, shoe):
        super().__init__(shoe)
        self.player_stand = False
        self.name = name

    
    def starting_cards(self):
        for i in range(2):
            c_card = self.shoe.shoe.pop() # Take the last card on the deck and remove it from the deck
            if c_card.rank == "Ace":
                self.ace_count += 1
            self.hand.cards.append(c_card) # Add the card to the hand
            self.hand.hand_total += c_card.value # Add the value to the total value of cards we hold
    
    def hit(self):
        hit_card = self.shoe.shoe.pop()
        if hit_card.rank == "Ace":
            self.ace_count += 1

        self.hand.cards.append(hit_card)
        self.hand.hand_total += hit_card.value
    
    def calculate_value(self):
        if self.hand.hand_total > 21:
            if self.ace_count:
                self.hand.hand_total -= 10
                self.ace_count -= 1
                return False
            else:
                self.bust = True
                return True # Player busted
    
    def stand(self):
        self.player_stand = True # Player stands

class Dealer(Participator):
    def __init__(self, name, shoe):
        super().__init__(shoe)
        self.hide_card = True
        self.name = name

    
    def get_visible_card(self):
        if self.hide_card:
            return self.hand.cards[0]
    
    def starting_cards(self):
        for i in range(2):
            c_card = self.shoe.shoe.pop() # Take the last card on the deck and remove it from the deck
            if c_card.rank == "Ace":
                self.ace_count += 1
            self.hand.cards.append(c_card) # Add the card to the hand
            self.hand.hand_total += c_card.value # Add the value to the total value of cards we hold
    

    def calculate_value(self):
        if self.hand.hand_total > 21:
            if self.ace_count:
                self.hand.hand_total -= 10
                self.ace_count -= 1
                return False
            else:
                self.bust = True
                return True # Dealer busted
    
    def hit(self):
        hit_card = self.shoe.shoe.pop()
        if hit_card.rank == "Ace":
            self.ace_count += 1

        self.hand.cards.append(hit_card)
        self.hand.hand_total += hit_card.value

class Game:
    def __init__(self, names: list = ["Aiden"]):
        self.players = []
        self.shoe: Deck = Deck()
        self.shoe.create_deck
        self.shoe.shuffle()
        for  i in names:
            self.players.append(Player(i, self.shoe))
        self.dealer: Dealer = Dealer("Jack", self.shoe)
        self.dealer_bust = False
        self.favorPlayer = "Akrom"

    def run(self):
        self.dealer.starting_cards()
        for i in self.players:
            i.starting_cards()

        for player in self.players:
            if player.name == "Akrom":
                while player.hand.hand_total < 21:
                    hitst = self.SmartPlay(gamer = player)
                    if hitst:
                        player.hit()
                        if player.hand.hand_total > 21:
                            if player.calculate_value():
                                break

                    else:
                        break
            else:
                hitst = np.random.choice([1, 0])
                while hitst:
                    player.hit()
                    hitst = np.random.choice([1, 0])

                    if player.hand.hand_total > 21:
                        bust = player.calculate_value()
                        if bust:
                            break  # Player busted, end their turn
                        else:
                            continue  # Ace was flipped, re-check total
                    
        # Dealer's turn
        self.dealer.hide_card = False
        dealer_hand = self.dealer.hand.hand_total
        while dealer_hand <= 16:
            self.dealer.hit()
            dealer_hand = self.dealer.hand.hand_total
            if dealer_hand > 21:
                bust = self.dealer.calculate_value()
                if bust:
                    self.dealer_bust = True
                    break
                else:
                    dealer_hand = self.dealer.hand.hand_total
                    continue
    
    def SmartPlay(self, gamer: Player):
        global under_16, under_4, dealer_prob
        if gamer.hand.hand_total <= 16:
            under_16 += 1
            return True
        hand_val = gamer.hand.hand_total
        # print(f"Akrom hand: {hand_val}")
        margin = 21 - hand_val
        deck_len = len(self.shoe.shoe)
        bust_nums = 0
        dealer_hands = self.dealer.get_visible_card().value
        card_values = [card.value for card in self.shoe.shoe]
        std = np.std(card_values)
        average = np.mean(card_values)

        # Calculating the probability of busting
        for i in self.shoe.shoe:
            if i.rank == "Ace" or i.value <= margin:
                continue
            if i.value > margin:
                bust_nums += 1
        
        chance = bust_nums/deck_len
        if chance < 0.4:
            under_4 += 1
            return True 
        
        
        if dealer_hands + average + std > 16:
            dealer_hand_total = dealer_hands + average + std

        
        else:
            dealer_hand_total = dealer_hands + (average * 2) + std
            
        if gamer.hand.hand_total < dealer_hand_total and chance < 0.7:
            dealer_prob += 1
            return True

       
        #     return True
    
    def FinalResult(self):
        global win_rate, lose_rate, bust_rate
        winners = []
        busters = []
        losers = []
        ties = []
        if self.dealer_bust:
            # print(self.dealer.hand.hand_total)
            if self.players[3].bust == False:
                win_rate += 1
            # print("Dealer busted")
            return
        for player in self.players:
            if player.hand.hand_total <= 21:
                if player.hand.hand_total > self.dealer.hand.hand_total:
                    winners.append(player.name)
                elif player.hand.hand_total == self.dealer.hand.hand_total:
                    ties.append(player.name)
                else:
                    losers.append(player.name)
            else:
                busters.append(player.name)
        
        # print(f"Dealer: {self.dealer.hand.hand_total}")
        # for i in self.players:
            # print(f"{i.name}: {i.hand.hand_total}")

        # print("Winners:")
        for i in winners:
            if i == "Akrom":
                win_rate += 1
            # print(i)
        
        # print("Ties:")
        # for i in ties:
            # print(i)
        
        # print('Losers:')
        for i in losers:
            if i == "Akrom":
                lose_rate += 1
            # print(i)
        
        # print("Busters:")
        for i in busters:
            if i == "Akrom":
                bust_rate += 1
            # print(i)
                
def PlayBlackjack():
    players = ["Aiden", "Clara", "Alex", "Akrom"]
    Blackjack: Game = Game(players)
    Blackjack.run()
    Blackjack.FinalResult()

bust_rate = 0
win_rate = 0
lose_rate = 0
under_16 = 0
under_4 = 0
dealer_prob = 0

games = 10000
if __name__ == "__main__":
    for _ in range(games):
        PlayBlackjack()

print(f"Win rate: {win_rate/games}\nLose rate: {lose_rate/games}\nBust rate: {bust_rate/games}")
print(f"<=16: {under_16}\n<0.4: {under_4}\nDealer statistics: {dealer_prob}")