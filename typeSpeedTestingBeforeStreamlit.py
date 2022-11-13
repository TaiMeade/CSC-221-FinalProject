"""

Tai Meade
CSC 221
Create a game that allows a user to practice their typing speed by typing a paragraph while being timed

"""

# import time
import random
import datetime

# def counter(endCondition):
#     t = 0
#     while endCondition != 1:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         time.sleep(1)
#         t += 1     
#     return timer

def startGame():
    start = input('Are you ready to start (y/n)? ')
    start = start.lower()
    while (start != "y") and (start != "n"):
        print("That is not a valid input. Please try again")
        start = input('Are you ready to start (y/n)? ')       
    return start.lower()


def main():

    thingsToType = {
                    "words":[
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

                    "sentences":[
                                "The brown cow decided to jump over the moon, shortly after the werewolf chased it for nearly 12 miles.",
                                "There was a random person named Jerry Jougenhopper that created the art of persuausion. Yes, this sentence is fictional.",
                                "Many people believe that the Marvel Cinematic Universe's movies are significantly better than the DC Universe movies. These people are right.",
                                "Back in high school, I used to go to Chemistry class and learn about Chemistry. For some reason, I would then go to my Gym class and learn about how to take a dodgeball to the face without crying...",
                                "I used to be one of the cool kids in high school. Now, I'm just a guy who used to be a cool kid in high school.",
                                "I love playing video games. I always have and I always will. I'm not addicted to anything, you are.",
                                "These sentences are getting dumber by the minute. Thank you for playing my TypeSpeedTester though!",
                                "Sometimes you need to be tested so good luck typing 2$#:'%$@fd12%* quickly and accurately!"

                    ]
    }

    start = startGame()
    if start == 'y':
        
        wordOrSentence = input("Would you like to type a really long, abstract WORD, or type a random SENTENCE from our lists? ").lower()

        while wordOrSentence != 'word' and wordOrSentence != 'sentence':
            print("That is not a valid input. Please try again.")
            wordOrSentence = input("Please choose either WORD or SENTENCE: ")

        if wordOrSentence == 'word':
            goalToType = random.choice(thingsToType["words"])
        elif wordOrSentence == 'sentence':
            goalToType = random.choice(thingsToType["sentences"])
        else:
            print("ERROR")

        print("\n------------------------------------------------------------------\n")
        print(f"Your goal is to type: \n{goalToType}")
        print("\n------------------------------------------------------------------\n")
        
        userInput = ""

        # Starts time
        startTime = datetime.datetime.utcnow()

        while userInput != goalToType:

            userInput = input("BEGIN: ")
            if userInput == goalToType:
                endTime = datetime.datetime.utcnow()
                timeTaken = ((endTime - startTime).total_seconds())
                
            else:
                print("That was incorrect. Please try again.")
                continue
        
        print(f"It took you {timeTaken:.2f} seconds to complete this.")

        lettersPerSecond = len(goalToType) / timeTaken

        print(f"That's approximately {lettersPerSecond:.2f} letters per second!\n")


    else:

        print("\nYou have successfully terminated the program.\n")

if __name__ == '__main__':
    
    main()