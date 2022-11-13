"""

Tai Meade
CSC 221
Final Project "The Odyssey" streamlit implementation

"""

import messageEncrypterAndDecrypter as msgEAD
import madLibStreamlit as mL
import passwordGenerator as pG
import rockPaperScissors as rPS
import typeSpeedTesting as tST
import random
import streamlit as st
import requests


# Global code for webpage
# Sets page config
st.set_page_config(page_title="The Odyssey - Coding Edition", page_icon="binaryCodePic.png", layout='wide')

# Sidebar Title
st.sidebar.title("Options:")

# Sidebar Dropdown
option = st.sidebar.selectbox("Select Page:", ("Home", "Password Generator", "Message Encrypter/Decrypter", "Rock Paper Scissors", "MadLib Generator", "TypeSpeedTester"))


#------------------------------------------------------Home Page-----------------------------------------------------
if option == "Home":

    # Formatting for placing title and logo next to each other
    col1, col2 = st.columns(2)

    with col1:

        # For formatting
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # Dashboard Title
        st.write("---")
        st.title("The Odyssey - Coding Edition")

        # Dashboard Subheader
        st.subheader("Created By: Tai Meade")
        st.write("---")

        # Goal for website...outside of columns
        st.subheader("**Goal:**")
        st.markdown("This is Tai Meade's final project for CSC 221.  It will consist of multiple programs separated into different sections.  The goal of this website is to showcase my skills as a programmer while remaining as user-friendly as possible.")
        st.markdown("---")

    # Formatting to move image to right side next to title
    with col2:
        st.write("")
        st.image(image="binaryCodePic.png")

    with st.expander("Code for Home Page:"):
        st.code('''#------------------------------------------------------Home Page-----------------------------------------------------
if option == "Home":

    # Formatting for placing title and logo next to each other
    col1, col2 = st.columns(2)

    with col1:

        # For formatting
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # Dashboard Title
        st.write("---")
        st.title("The Odyssey - Coding Edition")

        # Dashboard Subheader
        st.subheader("Created By: Tai Meade")
        st.write("---")

        # Goal for website...outside of columns
        st.subheader("**Goal:**")
        st.markdown("This is Tai Meade's final project for CSC 221.  It will consist of multiple programs separated into different sections.  The goal of this website is to showcase my skills as a programmer while remaining as user-friendly as possible.")
        st.markdown("---")

    # Formatting to move image to right side next to title
    with col2:
        st.write("")
        st.image(image="binaryCodePic.png")
        ''')

#-----------------------------------------------Password Generator Page----------------------------------------------
elif option == "Password Generator":
    # Sets title of the page
    st.title(option)

    # Writes goal/what the page will do.
    st.write("This program creates a random password of a specific length (specified by the user).  It will then output the generated password to the user.")

    st.write("---")

    try:
        passwordLength = range(int(st.text_input("Please specify the length of the password you'd like to generate:")))
    
        generatedPassword = pG.passwordGenerator(passwordLength)

        st.write("---")

        st.markdown(f'Generated Password:')
        st.markdown(f'**{generatedPassword}**')
    except Exception:
        st.write("---")
        st.write("Please enter an integer.")

    # Expander showcasing code for this program/function...SHOUTOUT TO JACOB ALTIZER FOR THIS AMAZING IDEA
    with st.expander("Code (not all code for 'streamlitifying' it):"):
        st.code('''"""

Tai Meade
CSC 221
Generate a random password with a set amount of characters decided by the user

"""

# Import all necessary libraries
import random

def passwordGenerator(passwordLength):
    # Lists to get a random character from
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'
    specialCharacters = '!@#$%^&*()[]<>?/;:-_=+,."\'\\'
    numbers = '0123456789'

    password = ''

    # Runs through number of times decided by input from user
    for character in passwordLength:

        # Decides if character will be from uppercase list, lowercase list, special characters list, or numbers list
        index1 = random.randint(1,4)
        if index1 == 1:
            index2 = random.randint(0,(len(upperCase)-1))
            password = password + upperCase[index2]
        elif index1 == 2:
            index2 = random.randint(0,(len(lowerCase)-1))
            password = password + lowerCase[index2]
        elif index1 == 3:
            index2 = random.randint(0,(len(specialCharacters)-1))
            password = password + specialCharacters[index2]
        else:
            index2 = random.randint(0,(len(numbers)-1))
            password = password + numbers[index2]

    return password

# NOTE: Must be a range because it is a part of a for loop...if it is an int then it will not work because an int is "not iterable"
#passwordGenerator(passwordLength=range(int(input("Please enter the number of characters you'd like your password to contain: "))))

if __name__ == '__main__':
    passwordLength = int(input("Enter length of password: "))
    passwordGenerator(passwordLength)
        ''')



#--------------------------------------------Message Encrypter/Decrypter Page----------------------------------------
elif option == "Message Encrypter/Decrypter":
    # Sets title of the page
    st.title(option)

    # Writes goal/what the page will do
    st.write("This program is separated into two tabs.  The encrypter tab accepts a message that will be encrypted.  It then outputs the encrypted message and the password to place into the decrypter in order to decrypt the message.")

    tab1, tab2 = st.tabs(["Encrypter", "Decrypter"])

    with tab1:
        st.header("Message Encrypter: ")

        messageToBeEncrypted = st.text_input("Insert message here:", key="tab1")

        encryptedMessage = msgEAD.messageEncrypter(messageToBeEncrypted)

        st.write("---")

        if messageToBeEncrypted != "":
            st.write(f"Encoded Message: ")
            st.text(f"{encryptedMessage[0]}") # NOTE: Must use "st.text" because write and markdown don't format it properly...unfortunately, this does not allow text-wrapping. 
            st.write("---")
            st.write(f"Password:")
            st.text(f"{encryptedMessage[1]}")

    with tab2:
        st.header("Message Decrypter: ")

        messageToBeDecrypted = st.text_input("Insert message here:", key="tab2")
        passwordForDecrypting = st.text_input("Insert password:")

        decryptedMessage = msgEAD.messageDecrypter(messageToBeDecrypted, passwordForDecrypting)

        st.write("---")

        if (messageToBeDecrypted and passwordForDecrypting) != "":
            st.markdown(f"Here is your decrypted message:")
            st.markdown(f"**{decryptedMessage}**")

    # Expander showcasing code for this program/function...SHOUTOUT TO JACOB ALTIZER FOR THIS AMAZING IDEA
    with st.expander("Code (not all code for 'streamlitifying' it):"):
        st.code('''"""

Tai Meade
CSC 221
Encode a message for a user using one of five methods.  Output the password to use in the decrypter to decrypt the message properly.

"""

# Import all necessary libraries
import random

def messageEncrypter(message):

    # Decides the encrypter version to use
    encrypterVersion = random.randint(1,5)

    # Did a quick google search to determine what letters are the most common in the English language
    if encrypterVersion == 1:
        # Reverses the message (got method from w3schools)
        message = message[::-1]
        message = message.replace('a', '!^')
        message = message.replace('e', '8$2')
        message = message.replace('i', '3Vk')
        message = message.replace('o', 'k27')
        message = message.replace('t', '%3')
        message = message.replace('s', '4*')
        message = message.replace('r', '<>')
        message = message.replace('n', ' $@')
        password = "chocolate"
    elif encrypterVersion == 2:
        message = message.replace('a', '!^')
        message = message.replace('e', '8$2')
        message = message.replace('i', '3Vk')
        message = message.replace('o', 'k27')
        message = message.replace('t', '%3')
        message = message.replace('s', '4*')
        message = message.replace('r', '<>')
        message = message.replace('n', ' $@')
        password = "strawberry"
    elif encrypterVersion == 3:
        message = message.replace('a', 'dh')
        message = message.replace('e', '23d')
        message = message.replace('i', '5!')
        message = message.replace('o', '#@$')
        message = message.replace('t', '<>:')
        message = message.replace('s', '.<"')
        message = message.replace('r', '<:" ')
        message = message.replace('n', ' d5w')
        password = "vanilla"
    elif encrypterVersion == 4:
        message = message.replace('a', 'h5g')
        message = message.replace('e', 'g3')
        message = message.replace('i', '4^&')
        message = message.replace('o', '23()')
        message = message.replace('t', '(3^)')
        message = message.replace('s', '3^2')
        message = message.replace('r', ' 100_=10^2')
        message = message.replace('n', '^351')
        password = "coffee"
    elif encrypterVersion == 5:
        message = message[::-1]
        message = message.replace('a', '$235-*+')
        message = message.replace('e', '#&(@#$')
        message = message.replace('i', '#$*()')
        message = message.replace('o', '_#()')
        message = message.replace('t', '45/+=-')
        message = message.replace('s', '234D4$')
        message = message.replace('r', 'gs$sgas')
        message = message.replace('n', '48/*d')
        password = "mint chocolate chip"
    return message, password

def messageDecrypter(message,password):
    if password == 'chocolate':
        message = message.replace('!^', 'a')
        message = message.replace('8$2', 'e')
        message = message.replace('3Vk', 'i')
        message = message.replace('k27', 'o')
        message = message.replace('%3', 't')
        message = message.replace('4*', 's')
        message = message.replace('<>', 'r')
        message = message.replace(' $@', 'n')
        message = message[::-1]
        
    elif password == 'strawberry':
        message = message.replace('!^', 'a')
        message = message.replace('8$2', 'e')
        message = message.replace('3Vk', 'i')
        message = message.replace('k27', 'o')
        message = message.replace('%3', 't')
        message = message.replace('4*', 's')
        message = message.replace('<>', 'r')
        message = message.replace(' $@', 'n')
        
    elif password == 'vanilla':
        message = message.replace('dh', 'a')
        message = message.replace('23d', 'e')
        message = message.replace('5!', 'i')
        message = message.replace('#@$', 'o')
        message = message.replace('<>:', 't')
        message = message.replace('.<"', 's')
        message = message.replace('<:" ', 'r')
        message = message.replace(' d5w', 'n')
        
    elif password == 'coffee':
        message = message.replace('h5g', 'a')
        message = message.replace('g3', 'e')
        message = message.replace('4^&', 'i')
        message = message.replace('23()', 'o')
        message = message.replace('(3^)', 't')
        message = message.replace('3^2', 's')
        message = message.replace(' 100_=10^2', 'r')
        message = message.replace('^351', 'n')
        
    elif password == 'mint chocolate chip':
        message = message.replace('$235-*+', 'a')
        message = message.replace('#&(@#$', 'e')
        message = message.replace('#$*()', 'i')
        message = message.replace('_#()', 'o')
        message = message.replace('45/+=-', 't')
        message = message.replace('234D4$', 's')
        message = message.replace('gs$sgas', 'r')
        message = message.replace('48/*d', 'n')
        message = message[::-1]

    else:
        message = "Invalid password. *awkward whistling*"
    return message

if __name__ == '__main__':
    
    # For testing
    encryptedMessage = messageEncrypter(message=input("Insert your message here: "))
    print(encryptedMessage)
    decryptedMessage = messageDecrypter(message=input("Message: "),password=input("Password: "))
    print(decryptedMessage)

''')



#------------------------------------------------Rock Paper Scissors Page--------------------------------------------
elif option == "Rock Paper Scissors":
    # Sets title of the page
    st.title(option)

    # Displays goals of this program/section
    st.write("This program has two different versions...a normal rock paper scissors mode in which the user competes against the computer and an impossible mode.")

    # Allows user to select difficulty of the rock, paper, scissors game
    difficulty = st.sidebar.selectbox("Difficulty:", (["Normal", "Impossible"]))

    st.write("---")

    if difficulty == 'Normal':
        
        userInput = st.text_input("Choose (rock, paper, or scissors): ")

        outcome = rPS.rockPaperScissors(userInput)
        
        st.write("---")
        st.header(f"{outcome}")
        st.write("---")
        if outcome == "YOU LOSE!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    background-color: #530000;
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        if outcome == "YOU WIN!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    background-color: #1c0642;
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        if outcome == "YOU TIE!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    elif difficulty == 'Impossible':
        userInput = st.text_input("Choose (rock, paper, or scissors): ")

        outcome = rPS.rockPaperScissorsImpossibleMode(userInput)
        
        st.write("---")
        st.header(f"{outcome}")
        st.write("---")
        if outcome == "YOU LOSE!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    background-color: #530000;
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        if outcome == "YOU WIN!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    background-color: #1c0642;
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        if outcome == "YOU TIE!":
            st.markdown(
                """
                <style>
                .css-k1vhr4 {
                    text-align: center;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    # Expander showcasing code for this program/function...SHOUTOUT TO JACOB ALTIZER FOR THIS AMAZING IDEA
    with st.expander("Code (not all code for 'streamlitifying' it):"):
        st.code("""'''

Tai Meade
CSC 221
Rock paper scissors game with a normal mode and an actual impossible mode (friendly trolling)

'''

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
        """)



#--------------------------------------------------MadLib Generator Page---------------------------------------------
elif option == "MadLib Generator":
    
    # I struggled converting this page to Streamlit format so I made it a separate page entirely and then imported it which is why there is less code here for it...
    mL.main()

    # Expander showcasing code for this program/function...SHOUTOUT TO JACOB ALTIZER FOR THIS AMAZING IDEA
    with st.expander("Code:"):
        st.code("""'''

Tai Meade
CSC 221
Streamlitifying my previously made MadLib file

'''

import requests
import streamlit as st
import madLibs as mL

def main():

    # Sets title for the page
    st.title("MadLib Generator")

    # Writes the goal of the program
    st.write("This page/program uses the requests module to retrieve a random .json object from an open source GitHub that contains several MadLibs.")
    st.write("---")

    

    # Set columns
    col1, col2, col3 = st.columns([1,1,2])

    wantToKnow = st.sidebar.selectbox("Do you want to know the title to the MadLib?", (["Yes", "No"]))

    # This allows streamlit to store it separate...otherwise it reruns everytime the user changes the value of the comma separated choices
    if 'madLib' not in st.session_state:
        st.session_state.madLib = mL.getMadLib()

    with col1:
        if st.button("New MadLib"):

            # Gets random madlib
            st.session_state.madLib = mL.getMadLib()

        try:
            # Get title, blanks, and rest of the story...initialize variables
            madLibTitle = st.session_state.madLib['title']
            restOfStory = mL.getRestOfStory(st.session_state.madLib)

            if wantToKnow == 'Yes':
                # Tells the user the title of their MadLib
                st.write(f"The title of your MadLib is: _**{madLibTitle}**_")

            # Gets blank choices/parts of speech in order to fill in.
            blanks = mL.getBlanksList(madLib=st.session_state.madLib)

            # Get index and blank to create an ordered list of the blanks/parts of speech for the user to fill into the text box.
            for i, blank in enumerate(blanks):
                st.write(f"{i+1}. {blank}")
                if i == 12:     # This if statement is tell the program to begin formatting the 'blanks' into the next column for better readability to the user
                    tooManyThings = True
                    break
        except Exception:
            st.write(Exception)

    with col2:

        # Places rest of blanks into a separate column next to the other.
        try:
            # For formatting 
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            if tooManyThings:
                for i,blank in enumerate(blanks):
                    if i >= 13:
                        st.write(f"{i+1}. {blank}")

        except Exception as e:
            pass

            

            

        # Avoids error popping up upon opening of the page
        except Exception as e:
            st.write("")
            #st.write(e)

    with col3:
        # Area where user enters their comma separated list of entries for the madLib
        userDecisions = st.text_input("Separated choices (EX: orange, blue, red, yellow, etc.): ")

        #userDecisions = userDecisions.split()

        if userDecisions != "":

            userDecisions = userDecisions.split(", ")

            # Without this line the last portion of the MadLib is not printed to the screen
            helpWithFormatting = ""
            userDecisions.append(helpWithFormatting)   

            finalMadLib = mL.putTogetherStory(restOfStory, userDecisions)

            st.markdown("Here is the MadLib you created: ")
            st.markdown(finalMadLib)

    st.write("---")



if __name__ == '__main__':

    main()
        """)



#--------------------------------------------------TypeSpeed Tester Page---------------------------------------------
elif option == "TypeSpeedTester":
    # Sets title of the page
    st.title(option)

    # Writes the goal of the program/page
    st.write("This program's goal is to test the user's typing speed.  It will allow them to type from a list of long words, or from a list of sentences I came up with.  It will also track the amount of time it takes the user to do so and then output the amount of letters/characters they typed per second.")
    st.write("---")

    # Expander containing rules
    with st.expander("RULES/TIPS:"):
        st.text("""
                1.  All entries must match EXACTLY to the passage/word you are given.\n
                2.  All sentences are separated with a single space.\n
                3.  The WPM is calculated according to the universal formula: ((charactersTyped/5) / minutesTaken)\n
                4.  I STRONGLY suggest deleting your input before beginning a new game...otherwise it will force you to delete your previous answer.
        """)

    # Another one (similar to the madLib project) that I created separately...wish I had done this for every page instead of converting them in this file lol.
    tST.main()
    st.write("---")

# Expander showcasing code for this program/function...SHOUTOUT TO JACOB ALTIZER FOR THIS AMAZING IDEA
    with st.expander("Code:"):
        st.code("""'''

Tai Meade
CSC 221
Create a game that allows a user to practice their typing speed by typing a paragraph while being timed

'''

# import time
import random
import datetime
import streamlit as st

# Gets the word or sentence randomly that the user will need to type
def getThingToType():
    thingsToType = {
                        "word":[
                                "supercalifragilisticexpialidocious",
                                "pneumonoultramicroscopicsilicovolcanoconiosis",
                                "pseudopseudohypoparathyroidism",
                                "floccinaucinihilipilification",
                                "antidisestablishmentarianism",
                                "incomprehensibilities",
                                "honorificabilitudinitatibus",
                                "sesquipedalianism",
                                "xenotransplantation",
                                "incomprehensibility",
                                "floccinaucinihilipilification",
                                "hippopotomonstrosesquippedaliophobia"
                        ],

                        "sentence":[
                                    "The brown cow decided to jump over the moon, shortly after the werewolf chased it for nearly 12 miles.",
                                    "There was a random person named Jerry Jougenhopper that created the art of persuasion. Yes, this sentence is fictional.",
                                    "Many people believe that the Marvel Cinematic Universe's movies are significantly better than the DC Universe movies. These people are right.",
                                    "Back in high school, I used to go to Chemistry class and learn about Chemistry. For some reason, I would then go to my Gym class and learn about how to take a dodgeball to the face without crying...",
                                    "I used to be one of the cool kids in high school. Now, I'm just a guy who used to be a cool kid in high school.",
                                    "I love playing video games. I always have and I always will. I'm not addicted to anything, you are.",
                                    "These sentences are getting dumber by the minute. Thank you for playing my TypeSpeedTester though!",
                                    "Sometimes you need to be tested so good luck typing supercalifragilisticexpialidocious quickly and accurately!",
                                    "This sentence is going to be extremely long because I feel that your words per minute have been inflated, and along with them, your confidence. You must be reminded that typing is not meant to be fun or easy."
                        ]
    }

    wordVsSentence = ['word', 'sentence']
    wordOrSentence = random.choice(wordVsSentence)

    return random.choice(thingsToType[wordOrSentence])



def main():

    if 'goalToType' not in st.session_state:
        st.session_state.goalToType = ""

    if st.button("New Game"):

        # Starts New Game
        st.session_state.goalToType = getThingToType()

        # Start time
        st.session_state.startTime = datetime.datetime.utcnow()

    col1, col2 = st.columns(2)

    # Starts game if button has been pressed...thanks to session state it will also not refresh page unless button is pressed (by default it refreshes everytime that the user types something into the text input box)
    if st.session_state.goalToType != '':

        try:
            # Centers the "New Game" button once it has been pressed
            st.markdown(
                    '''
                    <style>
                    .css-1uqmt5j {
                    margin-left: 46.5%;
                    }
                    </style>
                    ''',
                    unsafe_allow_html=True
                )
            with col1:
                st.write("---")
                st.write(f"Your goal is to type:")
                st.write(st.session_state.goalToType)
                st.write("---")
            
                userInput = ""

                userInput = st.text_input("TYPE AS FAST AS POSSIBLE:")

            with col2:
                # Centers results and the user's goal to type...increases readability
                st.write("---")
                st.subheader("RESULTS:")
                st.markdown(
                    '''
                    <style>
                    .css-keje6w {
                    text-align: center;
                    }
                    </style>
                    ''',
                    unsafe_allow_html=True
                )

                if userInput == st.session_state.goalToType:
                    endTime = datetime.datetime.utcnow()
                    timeTaken = ((endTime - st.session_state.startTime).total_seconds())
                    minutesTaken = timeTaken / 60
                        
                elif userInput == "":
                    pass

                elif userInput != st.session_state.goalToType:
                    st.write("That was incorrect. I'm sorry, but you have failed this test.  Get better at typing lol.")
                    
            
                st.write(f"It took you {timeTaken:.2f} seconds to complete this.")

                # Simple letters/characters per second calculation
                lettersPerSecond = len(st.session_state.goalToType) / timeTaken

                # Formula for WPM according to Google
                wordsPerMinute = (len(st.session_state.goalToType) / 5) / minutesTaken

                st.write(f"That's approximately {lettersPerSecond:.2f} letters per second!")
                st.write(f"That's approximately {wordsPerMinute:.2f} words per minute!")
        
        except Exception as e:
            pass

if __name__ == '__main__':
    
    main()
        
        """)



# In case of error...should not be possible unless user manually changes the page selector names...could probably be avoided by assigning each choice an index instead of checking for string name
else:
    # Sets title of the page
    st.title("ERROR")