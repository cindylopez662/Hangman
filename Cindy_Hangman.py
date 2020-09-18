#get letter guesses
import random  

my_word_list = [
    ['d','o','g'],
    ['c','a','t'],
    ['s','u','n'],
    ['f', 'i', 'r', 'e'],
    ['m', 'a', 't', 't', 'e', 'r'],
    ['j', 'u', 'n', 'g', 'k', 'o', 'o', 'k'],
    ['s','p','h','y','n','x'],
    ['m','o','t','h','m','a','n']
] 

magic_word = random.choice(my_word_list)

correct_guesses = []

incorrect_guesses = []

hangman_body = ['head', 'torso', 'leg1', 'leg2', 'arm1', 'arm2', 'hair', 'foot1', 'foot2', 'eye1', 'eye2', 'smile']

current_hangman = []

while True:
    letter_guessed = input(f"Guess a letter in my {len(magic_word)} letter word:")

    if letter_guessed in magic_word:
        if letter_guessed in correct_guesses: 
            print("You have already guessed this letter")
            continue
        print("Yes, that is correct. Guess again:")
        correct_guesses.append(letter_guessed)  
    else: 
        print("That's wrong, try again") 
        incorrect_guesses.append(letter_guessed)
        current_hangman.append(hangman_body[len(current_hangman)])
    
    print("Correct Guesses:", (correct_guesses))
    print("Incorrect Guesses:", (incorrect_guesses))
    print("Current hangman:", current_hangman)

    if set(correct_guesses) == set(magic_word): 
        print("That's right! The word is", magic_word)
        break
    
    elif len(incorrect_guesses) >= len(hangman_body):
        print("You ran out of guesses!") 
        print("The word was", magic_word)
        break
 