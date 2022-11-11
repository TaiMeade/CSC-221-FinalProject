"""

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

