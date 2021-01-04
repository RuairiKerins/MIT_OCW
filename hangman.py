# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed_right = 0
    for char1 in secret_word:
       for char2 in letters_guessed:    
           if char1 == char2:
              letters_guessed_right+=1

    if len(secret_word)==letters_guessed_right:
      return True 
    else:
      return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    coded_word = []
    for char1 in secret_word:   
            if char1 in letters_guessed:
              coded_word.append(char1)
            else:
              coded_word.append("_ ")
    
    return "".join(coded_word)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = list(string.ascii_lowercase)
    for char1 in letters_guessed:   
      letters_not_guessed.remove(char1)

    return "".join(letters_not_guessed)

def guesses_remaining(guesses):
  guesses_remaining = guesses-6
  return guesses_remaining

def warnings_remaining(guesses):
  warnings_remaining = errors-3
  return warnings_remaining
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the hangman game!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have 3 warnings maximum")
    guesses = 0
    letters_guessed = []
    correct_letters = []
    errors = 0
    vowels = ["a", "e", "i", "o", "u"]
    while guesses < 6 and errors < 3 and is_word_guessed(secret_word,letters_guessed)==False:
        print("   -------------------   ")
        print("You have",6 - guesses, "guesses left")
        remaining_letters=get_available_letters(letters_guessed)
        print("Available letters: ", remaining_letters)

        letter = (input("Please guess a letter: "))
        
        if str.isalpha(letter)==False:
            errors += 1
            print("Please enter a vaild guess. You have",errors,"!")
            

        if str.isalpha(letter) == True :
            letter = str.lower(letter)
            if letter in letters_guessed:
              errors += 1
              print("You've already guessed that letter. You now have",errors, "warnings:")
            else:
              if letter in secret_word:
                print("Good guess: ", end= "")
                correct_letters.append(letter)

              else:
                print("Bad guess: ", end= "")
                if letter in vowels:
                  guesses += 1
                guesses += 1
              letters_guessed.append(letter)
              print(get_guessed_word(secret_word, letters_guessed))

        

        if is_word_guessed(secret_word,letters_guessed) == True:
            print("You guessed the word!")
            score = (6-guesses)*len(correct_letters)
            print("You're score is",score,", good job!")
            
        
    if is_word_guessed(secret_word,letters_guessed)==False:
        print("You lose dirtbag! The word was",secret_word, "dummy")
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word, correct_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    correct_letters: list of correct letters guessed
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False if letters_gueesed dont show duplicate letters found in 
        other_word and not my_word and otherwise: 
    
    '''
    my_word = my_word.replace(" ","")
    letters_only = my_word.replace("_","")
    other_word.split()
    my_word.split()
    i = 0
    same_letter = 0
    letters_gueesed_myword = 0
    letters_gueesed_otherword = 0
    if len(my_word) == len(other_word):
      for char1 in other_word:                                  # makes sure duplicate letters are counted in other word
            if char1 in correct_letters:
              letters_gueesed_otherword +=1
      while i < len(my_word):                                   # makes sure letters are in same postion
          if my_word[i] == other_word[i]:
              same_letter += 1
          i += 1
      if len(letters_only) == same_letter and len(letters_only) is letters_gueesed_otherword :
          return True    

          
      else:
          return False




def show_possible_matches(my_word, correct_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for char in wordlist:
      result = match_with_gaps(my_word, char, correct_letters)
      #print(result)
      if result is True:
        possible_matches.append(char)
    print("The hidden wourd could be any of the following", *possible_matches, sep=", ")

    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("\033c", end="")
    print("Welcome to the hangman game!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have 3 warnings maximum")
    guesses = 0
    letters_guessed = []
    correct_letters = []
    errors = 0
    vowels = ["a", "e", "i", "o", "u"]
    partial_word = []
  
    while guesses < 6 and errors < 3 and is_word_guessed(secret_word,letters_guessed)==False:
        
        print("   -------------------   ")
        print("You have",6 - guesses, "guesses left and", errors, "warnings")
        remaining_letters=get_available_letters(letters_guessed)
        print("Available letters: ", remaining_letters)
        letter = (input("Please guess a letter: "))
        print("\033c", end="")


        if str.isalpha(letter) == False:
          if letter == "*":
              show_possible_matches(partial_word, correct_letters)
          else:
              errors += 1
              print("Please enter a vaild guess!")
          print(partial_word)
            

        if str.isalpha(letter) == True:
            letter = str.lower(letter)
            if letter in letters_guessed:
              errors += 1
              print("You've already guessed that letter. You now have",errors, "warnings:")
            else:
              if letter in secret_word:
                print("Good guess: ", end= "")
                correct_letters.append(letter)

              else:
                print("Bad guess: ", end= "")
                if letter in vowels:
                  guesses += 1
                guesses += 1
              letters_guessed.append(letter)
              partial_word = (get_guessed_word(secret_word, letters_guessed))
              print(partial_word)
        

        if is_word_guessed(secret_word,letters_guessed) == True:
            print("You guessed the word!")
            score = (6-guesses)*len(correct_letters)
            print("You're score is",score,", good job!")
            
        
    if is_word_guessed(secret_word,letters_guessed) is False:
        print("\033c", end="")
        print("You lose dirtbag! The word was",secret_word, "dummy")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = "marketable"
    hangman_with_hints(secret_word)
