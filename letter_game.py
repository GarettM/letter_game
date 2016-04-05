import random

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'line',
    'grapefruit',
    'lemon',
    'melon',
    'mango',
    'blackberry',
]

while True:
    start = input("Press enter to start or Q to quit")
    if start.lower() == 'q':
        break
    # pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        # # draw spaces, guessed letters and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
                
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')
    # take guess
        guess = input("guess a letter: ").lower()
        
        if len(guess) !=1:
            print("You can only guess one letter at a time.")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You guessed that already.")
        elif not guess.isalpha():
            print("Only letters!")
            continue
            
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)

    else:
        print("You didn't get it!  Secret word was {}".format(secret_word))
        
