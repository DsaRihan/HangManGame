# Hangman game
import random

WORDLIST_FILENAME ="Hangman Game/words.txt"


def loadWords():
    """Returns a list of valid words from file."""
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.readline().split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''Returns True if all letters in secretWord are guessed'''
    return all(letter in lettersGuessed for letter in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''Returns string with guessed letters and underscores'''
    return ''.join(letter if letter in lettersGuessed else '_ ' for letter in secretWord)

def getAvailableLetters(lettersGuessed):
    '''Returns string of unguessed letters'''
    import string
    return ''.join(letter for letter in string.ascii_lowercase if letter not in lettersGuessed)

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    mistakeMade = 0
    lettersGuessed = []
    
    while 8 - mistakeMade > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        print("-------------")
        print("You have", 8-mistakeMade, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()
        
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            mistakeMade += 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was", secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
