#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:50:15 2022

@author: paulbergeron
"""
# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 9

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}



WORDLIST_FILENAME = "words.txt"

def loadWords():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


def getWordScore(word, n):

    res = 0
    for letter in word:
        res += SCRABBLE_LETTER_VALUES[letter]
    if len(word) == n:
        res +=50
    return res


def displayHand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def dealHand(n):

    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


def updateHand(hand, word):

    handCopy = hand
    
    for item in word:
        if item in handCopy and (handCopy[item] > 0):
            handCopy[item] = handCopy.get(item, 0) - 1
    return handCopy


def isValidWord(word, hand, wordList):


    if word in wordList and all(c in hand for c in word):
        return True
    else:
        return False

def calculateHandlen(hand):

    def calculateHandlen(hand):

        return(sum(hand.values()))



def playHand(hand, wordList, n):

    score = 0
    
    # As long as there are still letters left in the hand:
    while sum(hand.values()) != 0:
       
        # Display the hand
        print("Current hand:"), displayHand(hand)
        
        # Ask user for input
        user_input = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if user_input == '.':
            
            # End the game (break out of the loop)
            print('Goodbye! Total score:', score, 'points. ')
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(user_input, hand, wordList) == False:
                
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.\n')
            
            # Otherwise (the word is valid):
            elif isValidWord(user_input, hand, wordList) == True:
                
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = (score+getWordScore(user_input, HAND_SIZE))
                print(user_input, "earned", getWordScore(user_input, HAND_SIZE), 'points. Total:', score, 'points\n') 
                
                # Update the hand 
                updateHand(hand, user_input)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score            
    if sum(hand.values()) == 0:
        print('Ran out of letters. Total score:', score, 'points. ')
    

   

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    
    welcome_input = ''
    
    while welcome_input == 'r' or 'n':
        welcome_input = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        #assign a reply option outside of loop if the user types 'r'
        hand = dealHand(HAND_SIZE)
        
        # 'n' deals a new hand, plays game
        if welcome_input == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            
        #'r' replays last hand using variable assigned in 'n'
        if welcome_input == 'r':
            playHand(hand, wordList, HAND_SIZE)
            
        #'e' exits game
     
        if welcome_input == 'e':
            return 0
    
    
    
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
