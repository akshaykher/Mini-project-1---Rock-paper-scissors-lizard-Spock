# Rock-paper-scissors-lizard-Spock Game

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# Each beats the preceeding two and loses to the following two
# The Game computes the winner based upon the above rule between the player and the computer

import random 

def name_to_number(name):
    """
    This is a function that converts the selected 
    name to its corresponding number
    """
    if name == 'rock' :
        return 0
    elif name == 'Spock' :
        return 1
    elif name == 'paper' :
        return 2
    elif name == 'lizard' :
        return 3
    elif name == 'scissors' :
        return 4
    else :
        return 'Name entered is invalid'

       
def number_to_name(number):
    """
    This is a function that converts the selected 
    number to its corresponding name 
    """
    if number == 0 :
        return 'rock'
    elif number == 1 :
        return 'Spock'
    elif number == 2 :
        return 'paper'
    elif number == 3 :
        return 'lizard'
    elif number == 4 :
        return 'scissors'
    else :
        return "number entered is invalid"
    
    
def rpsls(player_choice): 
    """
    This is a function that computes the
    winner
    """
    # blank line to separate consecutive games
    print
    
    # display player's choice
    print "Player chooses",player_choice
    
    # convert the player's choice to player_number
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice)
    comp_choice = number_to_name(comp_number)
    
    # display computer's choice
    print "Computer chooses",comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # print winner 
    if difference == 0 :
        print "Player and computer tie!"
    elif difference == 1 or difference == 2 :
        print "Computer wins!"
    elif difference == 3 or difference == 4 :
        print "Player wins!"
    else :
        "Oops values entered incorrectly"
    
# values entered by player
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




