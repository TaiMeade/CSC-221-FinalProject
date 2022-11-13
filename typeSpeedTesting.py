"""

Tai Meade
CSC 221
Create a game that allows a user to practice their typing speed by typing a paragraph while being timed

"""

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
                    """
                    <style>
                    .css-1uqmt5j {
                    margin-left: 46.5%;
                    }
                    </style>
                    """,
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
                    """
                    <style>
                    .css-keje6w {
                    text-align: center;
                    }
                    </style>
                    """,
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