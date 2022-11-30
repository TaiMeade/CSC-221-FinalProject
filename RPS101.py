"""

Tai Meade
Rock, paper, scissors with 101 possible choices...thankfully this one has an API

"""

import requests
import streamlit as st
import random

def getChoices():
    rps101Choices = requests.get("https://rps101.pythonanywhere.com/api/v1/objects/all")
    rps101Choices = rps101Choices.json()

    return rps101Choices

def getComputerChoice(listOfChoices):
    computerChoice = random.choice(listOfChoices)

    return computerChoice
    
def main():

    col1,col2 = st.columns(2)

    with col1:
        st.title("RPS 101")
        st.subheader("Rock, paper, scissors, but with 101 choices!")

    with col2:
        st.subheader("Disclaimer/Notes:")
        st.write("I did not create this!")
        st.write("* Also, in terms of making sense...this one is even WORSE than RPS 25.")
        st.write("* Another big fact to take away from this project is that you should ALWAYS search for APIs on something before creating something like this! This API finds the outcome for you, rather than coding a ridiculous amount yourself!")

    # Create list of all choices
    rps101Choices = (getChoices())

    # Gets random choice from all 101 options for computer
    computerChoice = getComputerChoice(rps101Choices)

    # Allows user to select from list of choices
    userChoice = st.selectbox("Please select your choice:", rps101Choices)

    # Check for match result
    result = requests.get(f"https://rps101.pythonanywhere.com/api/v1/match?object_one={userChoice}&object_two={computerChoice}")
    result = result.json()
    winner = result['winner']
    outcome = result['outcome']
    loser = result['loser']

    # Output outcome to screen
    if userChoice == winner:
        st.subheader("YOU WIN!")
        st.write(f"You picked {userChoice} and the computer picked {computerChoice}.  {winner} {outcome} {loser}.")
    elif computerChoice == winner:
        st.subheader("YOU LOSE")
        st.write(f"You picked {userChoice} and the computer picked {computerChoice}.  {winner} {outcome} {loser}.")
    else:
        st.write("DRAW")

if __name__ == '__main__':
    main()