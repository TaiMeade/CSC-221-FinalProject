"""

Tai Meade
CSC 221
Creating a Mad Libs game that gets a random mad lib story with blanks.
NOTE: Did not realize I would be using requests for this, but hopefully I can figure it out!  Also I'm using an API frm "HermanFassett" on GitHub...it has 16, well technically 17 potential MadLib stories

"""

import requests

def getMadLib():
    madLib = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25")
    madLib = madLib.json()
    return madLib

def getBlanksList(madLib):
    blanks = []
    for blank in madLib['blanks']:
        blanks.append(blank)
    return blanks

# Gets the user's decisions that will replace the blanks later on
def getUserChoices(blanks):
    userDecisions = []
    for blank in blanks:
        userDecision = input(f"Enter a {blank}: ")
        userDecision = userDecision.strip()
        userDecisions.append(userDecision)
    
    return userDecisions

# Gets the 'values' from madLib...which is the rest of the story/the non-blanks of the story
def getRestOfStory(madLib):
    restOfStory = madLib['value']
    return restOfStory

# Puts together the rest of the madlib in a readable/sentence format.
def putTogetherStory(restOfStory, userDecisions):
    finalMadLib = [i + j for i,j in zip(restOfStory, userDecisions)]    # NOTE: I did not know how to concatenate two lists by index, so I used Google and found a line EXTREMELY similar to this
    finalMadLib = ''.join(finalMadLib)
    return finalMadLib

# Main function...where all actual running of the code/declaration of variables is done
def main():

    print("\n---------WELCOME TO MY MADLIB GENERATOR!----------\n")

    # Gets the random madlib and stores it as madLib
    madLib = getMadLib()

    # Get title, blanks, and rest of the story...initialize variables
    madLibTitle = madLib['title']
    blanks = getBlanksList(madLib)
    restOfStory = getRestOfStory(madLib)

    # Tells the user the title in case they want to attempt to match the theme
    print("The title of your MADLIB is: " + madLibTitle + "\n")

    # Gets the user's choices for the blanks
    userDecisions = getUserChoices(blanks)

    # Combines the rest of the story with the user's choices
    finalMadLib = putTogetherStory(restOfStory, userDecisions)

    print(f"\nHere is the MADLIB you created:\n\n{finalMadLib}\n")

if __name__ == '__main__':
    main()