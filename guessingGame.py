"""

Tai Meade
CSC 221
Create number guessing game that works in streamlit

"""

import streamlit as st
import random

def guessingGame(newGame, maxNumber, userGuess):

    answer = random.randint(1,maxNumber)
    
    while int(userGuess) != answer:
        if int(userGuess) > answer:
            st.write(f"{userGuess} is too high!")
        elif int(userGuess) < answer:
            st.write(f"{userGuess} is too low!")
    else:
        st.write(f"YOU GOT IT RIGHT. The number was {answer}!")


newGame = st.button("New Game")
if newGame == True:
    maxNumber = st.slider("Max number:",10,100)
    userGuess = st.text_input("Enter your guess:")
    guessingGame(newGame,maxNumber,userGuess)