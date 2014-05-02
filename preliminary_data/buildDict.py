# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# 6 hours :(

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = random.randrange(2,5)

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "workcity.txt"
n = HAND_SIZE

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist
    print wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    i = 0
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
        i = i+1
    print freq
    return freq

	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first go.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # 40 minutes
    i = 0
    wordValue = 0
    wordAsList = list(word)
    for i in range(len(word)):
        currentLetter = wordAsList[i]
        currentLetterValue = SCRABBLE_LETTER_VALUES[currentLetter]
        wordValue = wordValue+currentLetterValue
    wordValue = wordValue*len(word)
    if len(word) == n:
        wordValue = wordValue +50
        print "all letters are used, extra 50 = ", wordValue
    return wordValue

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line
    

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # freqs: dictionary (element_type -> int)
    #30min
    wordAsList = list(word)
    i=0
    newhand = hand.copy()
    for i in range(len(word)):
        currentLetter = wordAsList[i]#get letter to take out
        newhand[currentLetter]= newhand[currentLetter]-1
    return newhand

    

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #30min
    valid = True                            #set to return true
    newhand = hand.copy()
    if word in word_list:                   # if not in list
        for i in list(word):                #iterate through each letter of word
            if i not in newhand.keys():     #if not in hand
                valid = False
            else:
                if newhand[i] ==0:          # if number of letter in hand is 0
                    valid = False
                newhand[i]= newhand[i]-1    #subtract amount of that letter by 1
    else:
        valid = False
    return valid
        
# Problem #4: Playing a hand

def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = len(hand)
    return handLen

#hand={'a':1, 's':1, 't':2, 'w':1, 'f':1, 'o':1}
#hand={'a':1, 'c':1, 'i':1, 'h':1, 'm':2, 'z':1}
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function
    # Keep track of two numbers: the number of letters left in your hand and the total score
    score = 0
    #hand = deal_hand(n)
    print "Current Hand:"
    display_hand(hand)                                                      # Display the hand  
    handLen = calculate_handlen(hand)
    while handLen > 0:                                                     # As long as there are still letters left in the hand:
        word = raw_input("enter a word or a . to indicate that you are finished ")  # Ask user for input
        if word == ".":                                                             # If the input is a single period:          
            break                                                        # End the game (break out of the loop)
            
        else:                                                               # Otherwise (the input is not a single period):
            if is_valid_word(word, hand, word_list) == False:               # If the word is not valid:
                print "Invalid Word, please try again"
                print "Current Hand:"
                display_hand(hand)
            else:                                                           # Otherwise (the word is valid):
                wordValue = get_word_score(word, n)                         # Tell the user how many points the word earned, and the updated total score 
                print word, "earned", wordValue, "points"
                hand=update_hand(hand, word)                                # Update hand and show the updated hand to the user
                print "Current Hand:"
                display_hand(hand)
                handLen = handLen-len(word)
                score = score + wordValue
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Total:", score, "points"
    
#
# Problem #5: Playing a game
# 

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, ask them again.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = random.randrange(7, 15)
    hand = deal_hand(n)

    # TO DO ... <-- Remove this comment when you code this function
    while True:   
        choice = raw_input("please input a letter, 'n', 'r', or 'e'")
        
        while choice !='n' and choice!='r' and choice!='e':
            choice = raw_input("please input a letter, 'n', 'r', or 'e'")
            
        if choice == 'n':
            n = random.randrange(7, 15)
            hand = deal_hand(n)
            play_hand(hand, word_list)
           
        if choice == 'r':
            play_hand(hand, word_list)
                      
        if choice == 'e':
            print "done"
            break
        


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    get_frequency_dict(word_list)
    print freq

