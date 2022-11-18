"""

Tai Meade
CSC 221
Streamlitifying my previously made MadLib file

"""

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
                if i == 12:
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

        try:
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
            
        except Exception as e:
            st.write(f"You have more than {len(blanks)} blanks!")

    st.write("---")


    






if __name__ == '__main__':

    main()