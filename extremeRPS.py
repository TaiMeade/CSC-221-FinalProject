"""

Tai Meade
CSC 221
Super complicated Rock Paper Scissors attempt found on Reddit

"""

import streamlit as st
import random
import images


def main():

    col1,col2 = st.columns(2)
  
    outcome = ""
    
    with col1:
        # Title of page
        st.title("RPS 25 - A fun way to learn about probability.")
        st.write("Rock paper scissors with 25 total choices.  I did not create this game, but I recreated it within Python (LOTS OF CONDITIONAL STATEMENTS LOL).  This game is intended to help the user understand some concepts of probability, whilst learning a new game and enjoying themselves.  It may also help the user learn some techniques to developing this type of game.")
        st.write("---")

        # Facts of the game
        st.subheader("Educational Facts:")
        st.write("* This version of 'rock, paper, scissors' contains 25 unique gestures that can be chosen.  This means that there are 325 total possible combinations (25 ties, and 300 in which one person loses) of gestures when 2 people are playing against one another.  However, within the code of this game, there are technically 625 possible combinations (25 ties and 600 in which one person loses).  This is because when coding a game like this (or at least the way I did it...), the order matters because the user's input must be checked first, then all subsequent possible choices for the computer/AI to make must also be checked.")
        st.write("* In order to make a game like this fair, each potential choice must win, and lose the same amount to all other choices.  In this case, 'Alien' (and all others) must win 12, lose 12, and tie with itself of course.  If a simple change such as 'Wolf beating Nuke' being changed to 'Nuke beating Wolf,' then the chance of winning by picking nuke would increase to being greater than all other choices, and subsequently make wolf the worst possible option.  Thus, some illogical terms were born.  In other words, when you lose to Wolf and you played Nuke, don't come crying to me lol.")
        st.write("* Of course, don't forget to enjoy the game, and the beautiful logo it's creator developed...P.S. there is now an RPS 101...")
        st.write("---")
        st.subheader("More Facts:")
        st.write("* There is a 1/25 (4%) chance of a tie")
        st.write("* This was painful to code the way I did it.")
        st.write("* Many of these conditions/scenarios make NO SENSE, but the game is still fun!")

    with col2:
        st.write("")
        st.write("")
        # Image from game...also image depicting rules/conditions
        st.image("images/RPS25Logo.jpg", use_column_width='always')
        with st.expander("**Game Conditions**"):
            st.image("images/RPS25Conditions.jpg")

    st.write("---")

    # Creates three columns...left, middle, right
    subCol1,subCol2,subCol3 = st.columns([1,1.5,1])

    # List of choices
    extremeRPSChoices = ['Nerf Gun','Dynamite','Nuke','Lightning','Devil','Dragon','Alien','Water','Bowl','Air','Moon','Paper','Sponge','Wolf','Cockroach','Tree','Man','Woman','Monkey','Snake','Axe','Scissors','Fire','Sun','Rock','']



    with subCol2:
        # Helps...does not make it impossible...decrease errors in user's input
        userInput = st.selectbox("Make your choice: ", extremeRPSChoices, 25)

        # List of choices for computer
        computerDecision = random.choice(extremeRPSChoices)

        # Checks for when user input and computer decision are the same...tie result
        if userInput == computerDecision:
            outcome = f"You both picked {userInput}! You TIED!"




        # Checks for when user input is 'Nerf Gun'
        elif userInput == 'Nerf Gun':
            if computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outclasses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outclasses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} inspires {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses a force-field against {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rusts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} splashes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tarnishes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is too far for {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outlaws {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleans {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} uses {computerDecision} as a target, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chips {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} destroys {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots at {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} uses {computerDecision} as a target, therefore you WIN!"



        # Checks for when user input is 'Dynamite'
        elif userInput == 'Dynamite':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outclasses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outclasses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} ignites {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} inspires {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} flosses with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} defuses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} douses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} splashes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blows out {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} suffocates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} encases {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} soaks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outruns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} starts a {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput}'s smoke blots out the {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} explodes {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Nuke'
        elif userInput == 'Nuke':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outclasses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outclasses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} defuses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} inspires {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} lived before {userInput}s, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} defuses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} short-circuits {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} encases the core of the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blows away {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is too far for {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} defines {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleans {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outruns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} survives {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} starts a massive {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} has the power of the {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} incinerates {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Lightning'
        elif userInput == 'Lightning':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} ignites {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} defuses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} casts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} conducts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} focuses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} creates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is too far for {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} defines {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} conducts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outruns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} hides from {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} attracts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} strikes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} strikes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} strikes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} strikes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} starts a {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput}'s storm blocks the {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} splits {computerDecision}, therefore you WIN!"




        # Checks for when user input is 'Devil'
        elif userInput == 'Devil':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} inspires {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} inspires {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} inspires {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} casts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} commands {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} does not believe in {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blesses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blesses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chokes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} terrifies {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rebukes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleanses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} bites {userInput}'s heiny, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} hides from {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} imprisons {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} exorcises {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tempts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} enrages {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} curses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hurls {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Dragon'
        elif userInput == 'Dragon':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} flosses with {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} lived before {computerDecision}s, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} commands {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} vaporizes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drowns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drowns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} freezes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shines on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rebukes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleanses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outruns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats {userInput}'s eggs, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shelters {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} slays {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} subdues {computerDecision}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chars {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} spawns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is immune to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blots out the {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rests upon {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Alien'
        elif userInput == 'Alien':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} uses a force field against {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} defuses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} defuses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shoots {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} doesn't believe in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} vaporizes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is toxic to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} forms around the alien's ship {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chokes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} houses {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} disproves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} intrigues {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chases {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} stows away with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} ensnares {userInput}'s ship, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} disproves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} disproves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} infuriates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} mutates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} uses a force field against {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} uses a force field against {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} stomps out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} destroys the {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} vaporizes {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Water'
        elif userInput == 'Water':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rusts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} douses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} short-circuits {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} conducts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blesses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drowns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is toxic to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} contains {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} evaporates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} has no {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} floats on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} absorbs {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}'s ship, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rusts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rusts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} puts out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} reflects {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} erodes {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Bowl'
        elif userInput == 'Bowl':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} splashes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} splashes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} encases the core of {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} focuses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blesses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drowns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} forms around {computerDecision}'s ship, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} holds {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tips over {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is too far for {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} avoids {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleans {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} drinks from {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} hides under {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses it's wood to create a {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats from a {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats from a {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} smashes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} sleeps in a {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chops {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} covers {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} snuffs out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} focuses the {computerDecision}'s rays, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} was once made of rock {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Air'
        elif userInput == 'Air':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tarnishes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blows out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blows {computerDecision} away, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} creates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chokes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} freezes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chokes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} evaporates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tips over {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} has no {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} fans {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} has {userInput} pockets, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} produces {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} flies through {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} swish through {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blows out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cools heat from the {computerDecision}'s rays, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} erodes {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Moon'
        elif userInput == 'Moon':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is too far for {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} suffocates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is too far for {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is far above {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} terrifies {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shines on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} houses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} has no {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is shaped like a {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} has no {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} surrounds {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} looks like {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} howls {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is nocturnal with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blocks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} travels {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} aligns with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} screeches at {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is nocturnal with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} reflects {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} reflects {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns a hole through {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eclipses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shines on {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Paper'
        elif userInput == 'Paper':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outlaws {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} encases {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} defines {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} defines {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rebukes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rebukes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} disproves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} floats on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} surrounds {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} fans {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} surrounds {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} soaks {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chews up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} nests between {userInput}s, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} creates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} writes on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} writes on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rips up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} nests in {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} slices {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cut {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shines through {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} covers {computerDecision}, therefore you WIN!"





        # Checks for when user input is 'Sponge'
        elif userInput == 'Sponge':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleans {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} soaks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleans {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} conducts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleanses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleanses {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} intrigues {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} absorbs {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleans {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} has {computerDecision} pockets, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} floods {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} soaks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chews up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} nests in {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} outlives {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleans with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleans with {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rips up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} swallows {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chops {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cuts up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} dries up {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"




        # Checks for when user input is 'Wolf'
        elif userInput == 'Wolf':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outruns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outruns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outruns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} bites {computerDecision}'s heiny, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outruns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chases {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} howls at {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chews up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chews up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} sleeps in fur of {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shelters {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tames {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tames {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} enrages {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} bites {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleaves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cuts {userInput}'s hair, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} buns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Cockroach'
        elif userInput == 'Cockroach':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} survives {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hides from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hides from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats eggs of {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} stows away with {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hides under {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hides from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} nests between {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} nests in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} sleeps in fur of {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shelters {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} steps on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} steps on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chops {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} stab {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} squishes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Tree'
        elif userInput == 'Tree':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses {userInput} as a target, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} survives {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} imprisons {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shelters {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} ensnares {computerDecision}'s ship, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput}'s wood creates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} produces {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blocks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput}s create {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} outlives {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shelters {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shelters {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} plants {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} plants {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} lives in {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} lives in {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chops down {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} carve {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns down {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} feeds {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blocks {userInput}'s roots, therefore you LOSE!"





        # Checks for when user input is 'Man'
        elif userInput == 'Man':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} strikes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} exorcises {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} slays {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} disproves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} travels to {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} writes on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleans with {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tames {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} steps on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} plants {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tempts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} flings poop at {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} bites {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleaves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cut {userInput}'s hair, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Woman'
        elif userInput == 'Woman':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} strikes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} tempts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} subdues {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} disproves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} aligns with {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} writes on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleans with {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tames {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} steps on {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} plants {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} tempts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} flings poop at {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} bites {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleaves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cut {userInput}'s hair, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Monkey'
        elif userInput == 'Monkey':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} strikes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} enrages {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chars {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} infuriates {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} smashes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} screeches at {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rips up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} rips up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} enrages {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} lives in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} flings poop at {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} flings poop at {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} bites {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cleaves {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} stab {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Snake'
        elif userInput == 'Snake':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} strikes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eats {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} spawns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} mutates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} drinks {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} sleeps in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} breathes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} hides from {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} nests in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} swallows {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} bites {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} eats {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} lives in {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} bites {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} bites {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} bites {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chops {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} stab {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} burns {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} warms {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} crushes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Axe'
        elif userInput == 'Axe':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chips {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses a force field against {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rusts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chops {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} flies through {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} reflects {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} slices {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chops {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleaves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chops {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chops down {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleaves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleaves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cleaves {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chops {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} are sharper than {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} forges {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} chips {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Scissors'
        elif userInput == 'Scissors':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} destroys {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses a force field against {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rusts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} covers {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} swish through {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} reflects {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cut {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cut up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cut {computerDecision}'s hair, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} stab {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} carve {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cut {computerDecision}'s hair, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} cut {computerDecision}'s hair, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} stab {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} stab {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} are sharper than {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} melts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} smashes {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Fire'
        elif userInput == 'Fire':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is immune to {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} starts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} starts a massive {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} starts {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} stomps out {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} puts out {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} snuffs out {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} blows out {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns a hole through {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns down {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} burns {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} forges {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} is made of {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} pounds out {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Sun'
        elif userInput == 'Sun':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shoots at {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision}'s smoke blots out the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} has the power of the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision}'s storm blocks the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} breathes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} destroys {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} reflects {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} focuses the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} cools the heat from the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} eclipses the {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} shines through {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} dries up {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} feeds {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} warms {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} melts {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} is made of {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[24]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shades {userInput}, therefore you LOSE!"





        # Checks for when user input is 'Rock'
        elif userInput == 'Rock':
            if computerDecision == extremeRPSChoices[0]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} uses {userInput} as a target, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[1]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} explodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[2]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} incinerates {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[3]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} splits {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[4]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} hurls {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[5]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} rests upon {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[6]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} vaporizes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[7]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} erodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[8]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} was once made of {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[9]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} erodes {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[10]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shines on {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[11]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} covers {userInput}, therefore you LOSE!"
            elif computerDecision == extremeRPSChoices[12]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[13]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[14]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} squishes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[15]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} blocks {computerDecision}'s roots, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[16]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[17]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[18]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[19]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} crushes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[20]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} chips {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[21]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} smashes {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[22]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {userInput} pounds out {computerDecision}, therefore you WIN!"
            elif computerDecision == extremeRPSChoices[23]:
                outcome = f"You picked {userInput} and the computer picked {computerDecision}.  {computerDecision} shades from the {userInput}, therefore you WIN!"



        # Statements to catch errors if any ever occur
        elif userInput == "":
            outcome = ""
        else:
            outcome = "Invalid input."

        # REMOVE EVENTUALLY
        # st.write(userInput,computerDecision)
        
        # Writes outcome to screen
        st.write(outcome)

        # Checks to see what to put for images
        if userInput != "":
            if userInput == extremeRPSChoices[0]:
                userImage = "images/nerf_gun.png"
            elif userInput == extremeRPSChoices[1]:
                userImage = "images/dynamite.png"
            elif userInput == extremeRPSChoices[2]:
                userImage = "images/nuke.png"
            elif userInput == extremeRPSChoices[3]:
                userImage = "images/lightning.png"
            elif userInput == extremeRPSChoices[4]:
                userImage = "images/horns.png"
            elif userInput == extremeRPSChoices[5]:
                userImage = "images/dragon.png"
            elif userInput == extremeRPSChoices[6]:
                userImage = "images/alien.png"
            elif userInput == extremeRPSChoices[7]:
                userImage = "images/water.png"
            elif userInput == extremeRPSChoices[8]:
                userImage = "images/bowl.png"
            elif userInput == extremeRPSChoices[9]:
                userImage = "images/air.png"
            elif userInput == extremeRPSChoices[10]:
                userImage = "images/moon.png"
            elif userInput == extremeRPSChoices[11]:
                userImage = "images/paper.png"
            elif userInput == extremeRPSChoices[12]:
                userImage = "images/sponge.png"
            elif userInput == extremeRPSChoices[13]:
                userImage = "images/wolf.png"
            elif userInput == extremeRPSChoices[14]:
                userImage = "images/cockroach.png"
            elif userInput == extremeRPSChoices[15]:
                userImage = "images/tree.png"
            elif userInput == extremeRPSChoices[16]:
                userImage = "images/man.png"
            elif userInput == extremeRPSChoices[17]:
                userImage = "images/woman.png"
            elif userInput == extremeRPSChoices[18]:
                userImage = "images/monkey.png"
            elif userInput == extremeRPSChoices[19]:
                userImage = "images/snake.png"
            elif userInput == extremeRPSChoices[20]:
                userImage = "images/axe.png"
            elif userInput == extremeRPSChoices[21]:
                userImage = "images/scissors.png"
            elif userInput == extremeRPSChoices[22]:
                userImage = "images/fire.png"
            elif userInput == extremeRPSChoices[23]:
                userImage = "images/sun.png"
            elif userInput == extremeRPSChoices[24]:
                userImage = "images/rock.png"
            else:
                userImage = "images/error.png" #IF ERROR OCCURS

        # Checks for image setting for computer side
        if userInput != "":
            if computerDecision == extremeRPSChoices[0]:
                computerImage = "images/nerf_gun.png"
            elif computerDecision == extremeRPSChoices[1]:
                computerImage = "images/dynamite.png"
            elif computerDecision == extremeRPSChoices[2]:
                computerImage = "images/nuke.png"
            elif computerDecision == extremeRPSChoices[3]:
                computerImage = "images/lightning.png"
            elif computerDecision == extremeRPSChoices[4]:
                computerImage = "images/horns.png"
            elif computerDecision == extremeRPSChoices[5]:
                computerImage = "images/dragon.png"
            elif computerDecision == extremeRPSChoices[6]:
                computerImage = "images/alien.png"
            elif computerDecision == extremeRPSChoices[7]:
                computerImage = "images/water.png"
            elif computerDecision == extremeRPSChoices[8]:
                computerImage = "images/bowl.png"
            elif computerDecision == extremeRPSChoices[9]:
                computerImage = "images/air.png"
            elif computerDecision == extremeRPSChoices[10]:
                computerImage = "images/moon.png"
            elif computerDecision == extremeRPSChoices[11]:
                computerImage = "images/paper.png"
            elif computerDecision == extremeRPSChoices[12]:
                computerImage = "images/sponge.png"
            elif computerDecision == extremeRPSChoices[13]:
                computerImage = "images/wolf.png"
            elif computerDecision == extremeRPSChoices[14]:
                computerImage = "images/cockroach.png"
            elif computerDecision == extremeRPSChoices[15]:
                computerImage = "images/tree.png"
            elif computerDecision == extremeRPSChoices[16]:
                computerImage = "images/man.png"
            elif computerDecision == extremeRPSChoices[17]:
                computerImage = "images/woman.png"
            elif computerDecision == extremeRPSChoices[18]:
                computerImage = "images/monkey.png"
            elif computerDecision == extremeRPSChoices[19]:
                computerImage = "images/snake.png"
            elif computerDecision == extremeRPSChoices[20]:
                computerImage = "images/axe.png"
            elif computerDecision == extremeRPSChoices[21]:
                computerImage = "images/scissors.png"
            elif computerDecision == extremeRPSChoices[22]:
                computerImage = "images/fire.png"
            elif computerDecision == extremeRPSChoices[23]:
                computerImage = "images/sun.png"
            elif computerDecision == extremeRPSChoices[24]:
                computerImage = "images/rock.png"
            else:
                computerImage = "images/error.png" #IF ERROR OCCURS

        with subCol1:
            if userInput != "":
                st.subheader("User Decision:")
                st.image(userImage, use_column_width='always')


        with subCol3:
            if userInput != "":
                st.subheader("Computer Decision:")
                st.image(computerImage, use_column_width='always')

if __name__ == '__main__':

    main()