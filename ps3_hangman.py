
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



wordlist = loadWords()

print("Welcome to the game Hangman!")

def isWordGuessed(secretWord, lettersGuessed):

    result = all(elm in lettersGuessed for elm in ([*secretWord]))
    if result:
        return(True)
    else:
        return(False)

lettersGuessed = []

def getGuessedWord(secretWord, lettersGuessed):

    new_list = []
    for element in ([*secretWord]):
        if element in lettersGuessed:
            new_list.append(element)
        else:
            new_list.append(' _ ')
    return(''.join(str(x) for x in new_list))


def getAvailableLetters(lettersGuessed):

    import string
    alphabet = list(string.ascii_lowercase)
    alphabet = [x for x in alphabet if not x in lettersGuessed]
    return(''.join(str(x) for x in alphabet))



def hangman(secretWord):

    #Greet user
    print('I am thinking of a word that is', (len(secretWord)), "letters long.")
    #initialize guesses and lettersGuessed
    
    alreadyGuessed = []
    guessesLeft = 8
    
            
    while guessesLeft > 0:
        print('You have', guessesLeft, 'guesses left')
        
        print('Available letters:', getAvailableLetters(lettersGuessed))
        
        user_guess = input('Please guess a letter:')
        
        lettersGuessed.append(user_guess)

        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess:", secretWord)
            print("Congratulations, you won!")
            break


        if user_guess in alreadyGuessed:
            print("Oops! You've already guessed that letter:" , getGuessedWord(secretWord, lettersGuessed))
            print('\n')
    
        elif user_guess in secretWord:
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(user_guess)
            alreadyGuessed.append(user_guess)
            print('\n')

        elif user_guess not in secretWord:
            guessesLeft -=1
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(user_guess)
            alreadyGuessed.append(user_guess)
            print('\n')
    


