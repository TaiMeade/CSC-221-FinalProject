"""

Tai Meade
CSC 221
Rock paper scissors game with a normal mode and an actual impossible mode (friendly trolling)

"""

import streamlit as st
import random

def rockPaperScissors(userInput):
    
    # Helps prevent errors from being made based on user's input format
    userInput = userInput.lower().strip()
    
    # Generate decision for AI/computer
    computerDecisionIndex = random.randint(1,3)
    if computerDecisionIndex == 1:
        computerDecision = 'rock'
    elif computerDecisionIndex == 2:
        computerDecision = 'paper'
    else:
        computerDecision = 'scissors'
    
    # Logic for determining winner
    if userInput == 'rock' and computerDecision == 'rock':
        outcome = "YOU TIE!"
    elif userInput == 'rock' and computerDecision == 'paper':
        outcome = "YOU LOSE!"
    elif userInput == 'rock' and computerDecision == 'scissors':
        outcome = "YOU WIN!"
    elif userInput == 'paper' and computerDecision == 'rock':
        outcome = "YOU WIN!"
    elif userInput == 'paper' and computerDecision == 'paper':
        outcome = "YOU TIE!"
    elif userInput == 'paper' and computerDecision == 'scissors':
        outcome = "YOU LOSE!"
    elif userInput == 'scissors' and computerDecision == 'rock':
        outcome = "YOU LOSE!"
    elif userInput == 'scissors' and computerDecision == 'paper':
        outcome = "YOU WIN!"
    elif userInput == 'scissors' and computerDecision == 'scissors':
        outcome = "YOU TIE!"
    elif userInput == "":
        outcome = ""
    else:
        outcome = "I'm sorry, but that is not a valid input!"
    return outcome

# for testing
#rockPaperScissors(userInput=input("Please enter your choice of rock, paper, or scissors: "))

def rockPaperScissorsImpossibleMode(userInput):

    # Helps prevent errors from being made based on user's input format
    userInput = userInput.lower().strip()
    
    # Logic that makes the game LITERALLY impossible
    if userInput == 'rock':
        computerDecision = 'paper'
    elif userInput == 'paper':
        computerDecision = 'scissors'
    elif userInput == 'scissors':
        computerDecision = 'rock'
    else:
        outcome = "That is not a valid input"

    # Logic deciding winner (although it will/SHOULD always be the computer)
    if userInput == 'rock' and computerDecision == 'rock':
        outcome = "YOU TIE!"
    elif userInput == 'rock' and computerDecision == 'paper':
        outcome = f"YOU LOSE!"
    elif userInput == 'rock' and computerDecision == 'scissors':
        outcome = "YOU WIN!"
    elif userInput == 'paper' and computerDecision == 'rock':
        outcome = "YOU WIN!"
    elif userInput == 'paper' and computerDecision == 'paper':
        outcome = "YOU TIE!"
    elif userInput == 'paper' and computerDecision == 'scissors':
        outcome = "YOU LOSE!"
    elif userInput == 'scissors' and computerDecision == 'rock':
        outcome = "YOU LOSE!"
    elif userInput == 'scissors' and computerDecision == 'paper':
        outcome = "YOU WIN!"
    elif userInput == 'scissors' and computerDecision == 'scissors':
        outcome = "YOU TIE!"
    elif userInput == "":
        outcome = ""
    else:
        outcome = "I'm sorry, but that is not a valid input!"
    return outcome


