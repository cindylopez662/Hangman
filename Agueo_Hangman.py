''' hangman game ''' 
# We need a word
# need a game loop
# need to get guesses
# need to build the man
# condition for win or lose

# word to guess
my_word = ['c','a','t']

# A hang man
hang_man_t = ['head', 'torso', 'leg_l', 'leg_r', 'arm_l', 'arm_r']
current_hangman = []
body_index = -1

guessed_letters = []
correct_guessed_letters = []

# game loop
while True:
    # Get letter guesses
    letter_guessed = input('Guess a letter for the 3 letter word: ')

    # check if guess was correct
    if letter_guessed in my_word:
        #if was true
        print("Yes that letter was correct")
        correct_guessed_letters.append(letter_guessed)
    else: 
        # if was false
        print("Nope, try again")
        guessed_letters.append(letter_guessed)
        body_index += 1
        current_hangman.append(hang_man_t[body_index])
    
    # check if we won or if we lost
    if len(my_word) == len(correct_guessed_letters):
        print('You win!')
        break
    elif body_index == len(hang_man_t)-1:
        print("You lose!")
        break

    #print guessed letters and incorrect guessed letters and hangman
    print('Guessed letters: ', correct_guessed_letters)
    print('Incorrect Guesses: ', guessed_letters)
    print("Current hangman :", current_hangman)