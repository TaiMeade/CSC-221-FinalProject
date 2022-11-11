"""

Tai Meade
CSC 221
Final Project "The Odyssey" streamlit implementation

"""

import messageEncrypterAndDecrypter as msgEAD
import madLibs as mL
import passwordGenerator as pG
import rockPaperScissors as rPS
import typeSpeedTesting as tST
import random
import streamlit as st
import requests



# Sets page config
st.set_page_config(page_title="The Odyssey - Coding Edition", page_icon="binaryCodePic.png")

# Sidebar Title
st.sidebar.title("Options:")

# Sidebar Dropdown
option = st.sidebar.selectbox("Select Program:", ("Home", "Password Generator", "Message Encrypter/Decrypter", "Rock Paper Scissors", "MadLibs", "TypeSpeedTester"))



if option == "Home":
    # Dashboard Title
    st.title("The Odyssey - Coding Edition")

    # Dashboard Subheader
    st.subheader("Created By: Tai Meade")
    st.write("---")

    # Goal for website
    st.markdown("**Goal:**")
    st.markdown("This is Tai Meade's final project for CSC 221.  It will consist of multiple programs separated into different sections.  The goal of this website is to showcase my skills as a programmer while remaining as user-friendly as possible.")
    
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
        st.write("Please enter an integer.")

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

        st.markdown(f"Here is your decrypted message:")
        st.markdown(f"**{decryptedMessage}**")


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

    else:
        st.write("ERROR")

elif option == "MadLibs":
    # Sets title of the page
    st.title(option)

elif option == "TypeSpeedTester":
    # Sets title of the page
    st.title(option)

else:
    # Sets title of the page
    st.title("ERROR")