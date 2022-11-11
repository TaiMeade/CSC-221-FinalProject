"""

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