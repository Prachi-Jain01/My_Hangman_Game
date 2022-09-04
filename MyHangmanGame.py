import random

words = "ValidWords.txt"

def unpackingWords():
    """
    unpacks all the words(data type: strings) from ValidWords.txt file and put them in a list. 

    """
    print("GET READY, ROLL UP THAT SLEEVE! ;) ")
    
    # opening the ValidWords.txt file
    inFile = open(words, 'r')
    # here the "line" will be a string
    line = inFile.readline()
    # here the "list_words" is a list of the words
    list_words = line.split()
    print( "Tighten the seatbelt! " ,len(list_words), "words loaded.")
    return list_words

def chooseWord(list_words):
    """
    Returns a word (data type: string) randomly chosen from the list_words (structure: list).

    """
    return random.choice(list_words)

# -----------------------------------(. ❛ ᴗ ❛.)-----------------------------------

list_words = unpackingWords()

def isWordGuessed(secretWord, progress):
    '''
    secretWord (data type: string) -> word to be guessed
    progress (data structure: list) -> letters those have been guessed till now
    returns (data type: boolean):
        True if all the letters of secretWord are in progress;
        False otherwise
    '''
    c=0
    for i in progress:
        if i in secretWord:
            c+=1
    if c==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, progress):
    '''
    secretWord (data type: string) -> word to be guessed
    progress (data structure: list) -> letters those have been guessed till now
    returns (data type: string):
        String of underscores and correct letters guessed till now
    '''
    s=[]
    for i in secretWord:
        if i in progress:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(progress):
    '''
    progress (data structure: list) -> letters those have been guessed till now
    returns (data type: string):
        {alphabets} -'alphabets that have been guessed till now'
    '''
    import string
    ans=list(string.ascii_lowercase)
    for i in progress:
        ans.remove(i)
    return ''.join(ans)

def hangman(secretWord):
    '''
    secretWord (data type: string) -> word to be guessed

    Game begins
    * User is informed about the no.of letters in the word
    * User is given one guess per round
    * Inform the user immediately whether the guess is correct or not
    * After each round, Inform about the current status

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Lessgoo!")
    print("The word you should guess is ",len(secretWord)," letters long.")
    
    global progress
    counter_mistake=0
    progress=[]
    
    while 8 - counter_mistake > 0:
        
        if isWordGuessed(secretWord, progress):
            print("-------------(. ❛ ᴗ ❛.)-------------")
            print("Correct word!")
            break
            
        else:
            print("-----------------------------------")
            print("You have ",8-counter_mistake," guesses left.")
            print("Letters that can be used now: ",getAvailableLetters(progress))
            guess=str(input("Guess a letter: ")).lower()
            
            if guess in progress:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,progress))
                
            elif guess in secretWord and guess not in progress:
                progress.append(guess)
                print("Good guess:",getGuessedWord(secretWord,progress))
                
            else:
                progress.append(guess)
                counter_mistake += 1
                print("Oops! That letter is not the correct one:",getGuessedWord(secretWord,progress))
                
        if 8 - counter_mistake == 0:
            print("-------------")
            print("You ran out of guesses. The actual word is: ",secretWord)
            break
        
        else:
            continue


secretWord = chooseWord(list_words).lower()
hangman(secretWord)