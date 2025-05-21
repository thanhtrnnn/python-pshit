"""
A module for a very simple approximation of the game Blackjack

This module provides the class for the Blackjack game, but NOT the cards.  Those are
provided in the card module.

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import card
import random


class Blackjack(object):
    """
    A class representing the state of a game of blackjack with one player.
    
    INSTANCE ATTRIBUTES:
        playerHand: list of the Cards held by the player [list of Cards]
        dealerHand: list of the Cards held by the dealer [list of Cards]
        deck: list of the remaining Cards to draw from   [list of Cards]
        
    The deck attribute is assumed to hold enough Cards for the game 
    to be able to run to completion (i.e. the deck wil not run out 
    of cards for the player or dealer to draw).
    """
    
    def __init__(deck):
        """
        Initializer: Creates a new blackjack game with the two hands initialized.
        
        The player's hand playerHand will be the first two cards in deck.
        The dealer's hand dealerHand will be the third card in deck.  
        These three cards are removed from deck.
        
        Deck is a parameter because we allow the caller, such as a casino, 
        to "stack the deck" (choose the arrangement of the cards, insert 
        extra cards,etc.) to its advantage!
        
        Parameter deck: The deck (or 'shoe') to deal cards from
        Precondition: deck is a list of Card.  It contains at least three Cards 
        (more is preferable).
        """
        # ASSERT THE PRECONDITIONS (BEST YOU CAN)
        pass  # TODO: implement me, according to my spec
    
    def __str__():
        """
        Returns: the string <player's score>, <dealer's score>
        
        Here, we are assuming that all that matters is the score 
        (which is True if aces are always 11).
        
        Example output:
            'player: 12; dealer: 20'
        """
        pass  # TODO: implement me, according to my spec
    
    def dealerScore():
        """
        Returns: the score for the dealer.
        """
        pass  # TODO: implement me, according to my spec
    
    def playerScore():
        """
        Returns: the score for the player.
        """
        pass  # TODO: implement me, according to my spec
    
    def playerBust():
        """
        Returns: True if player has gone bust (score is over 21), and False otherwise
        """
        pass  # TODO: implement me, according to my spec
    
    def dealerBust():
        """
        Returns: True if dealer has gone bust (score is over 21), and False otherwise
        """
        pass  # TODO: implement me, according to my spec
    
    # HELPER METHODS (DO NOT MODIFY)
    def _score(self, hand):
        """
        Returns: a simplified-blackjack score for a given hand
        
        This is a helper method for computing the score of a given hand.  In our version 
        of blackjack, aces always count as 11 points.  Face cards count as 10 points and 
        Suits do not matter.
        
        Example: input: [2 of Hearts, Ace of spades], output: 13
        Example: input: [King of Diamonds, 3 of Clubs], output 13
        
        Parameter hand: The blackjack hand
        Precondition: hand is a list of Cards"""
        s = 0  # score to return
        for c in hand:
            if c.rank >= 11:  # c is a face card
                s = s + 10
            elif c.rank == 1:  # c is an ace
                s = s + 11
            else:
                s = s + c.rank
        return s


# DO NOT MODIFY BELOW THIS LINE

def playgame():
    """
    Creates and runs a new blackjack game.
    
    This function provides a text based interface for blackjack.
    It will continue to run until the end of the game.
    """
    
    # Create a new shuffled full deck
    deck = card.full_deck()
    random.shuffle(deck)
    
    # Start a new game. Player gets two cards; dealer gets one
    game = Blackjack(deck)
    
    # Tell player the scoring rules
    print('Welcome to CS 1110 Blackjack.')
    print('Rules: Face cards are 10 points. Aces are 11 points.')
    print('       All other cards are at face value.')
    print()
    
    # Show initial deal
    print('Your hand: ')
    card.print_cards(game.playerHand)
    print()
    print('Dealer\'s hand: ')
    card.print_cards(game.dealerHand)
    print()
    
    # While player has not bust, ask if player wants to draw
    player_halted = False  # True player wants to halt, False otherwise
    while not game.playerBust() and not player_halted:
        # ri: input received from player
        ri = _prompt_player('Type h for new card, s to stop: ',['h', 's'])
    
        player_halted = (ri == 's')
        if (not player_halted):
            game.playerHand.append(game.deck.pop(0))
            print('You drew the ' + str(game.playerHand[-1]))
            print()
    
    if game.playerBust():
        print('You went bust, dealer wins.')
    else:
        _dealer_turn(game)
    
    print()
    print('The final scores were ' + str(game))


def _prompt_player(prompt,valid):
    """
    Returns: the choice of a player from a given prompt.
    
    This is a helper function for playgame().  It asks the user a question, and waits 
    for a response.  It checks if the response is valid against a list of acceptable 
    answers.  If it is not valid, it asks the question again. Otherwise, it returns the 
    player's answer.
    
    This function has been factored out of playgame() to show good design.  Otherwise, 
    playgame() is a long and unreadable function.
    
    Parameter prompt: The question prompt to display to the player
    Precondition: prompt is a string
    
    Parameter valid: The valid reponses
    Precondition: valid is a list of strings 
    """
    # Ask the question for the first time.
    # ri: input received from player
    ri = input(prompt)
    
    # Continue to ask while the response is not valid.
    while not (ri in valid):
        print('Invalid response.  Answer must be one of ')+str(valid)
        print()
        ri = input(prompt)
    
    return ri


def _dealer_turn(game):
    """Performs the dealer's turn, printing out the result.
    
    The function uses standard BlackJack rules: the dealer
    stands above 17, but hits otherwise.
    
    This function has been factored out of play_a_game() to
    show good design.  Otherwise, play_a_game() is a long
    and unreadable function."""
    # Dealer draws until at 17 or above or goes bust
    while game.dealerScore() < 17 and not game.dealerBust():
        game.dealerHand.append(game.deck.pop(0))
        print('Dealer drew the ' + str(game.dealerHand[-1]))
     
    print()
    if (game.dealerBust()):
        print('Dealer went bust, you win!')
    elif (game.dealerScore() > game.playerScore()):
        print('Dealer outscored you, dealer wins.')
    elif (game.dealerScore() < game.playerScore()):
        print('You outscored dealer, you win!')
    else:
        print('The game was a tie.')

# Script code
if __name__ == '__main__':
    playgame()


