import random

Chances = 3

words = ['watermelon', 'banana', 'apple', 'orange', 'pineapple', 'peach', 'mango', 'strawberry', 'lychee', 'grape']
secret_fruit = random.choice(words)
clue = list('?' * len(secret_fruit))
heart_symbol = u'\u2764'

guessed_fruit_correctly = False

def update_clue(guessed_letter, secret_fruit, clue):
    index = 0
    while index < len(secret_fruit):
        if guessed_letter == secret_fruit[index]:
            clue[index] = guessed_letter
        index = index + 1

while Chances > 0:
    print(''.join(clue))
    print('Chances left: ' + heart_symbol * Chances)
    guess = input('Guess a letter or the whole word: ')

    if guess.lower() == secret_fruit:
        guessed_fruit_correctly = True
        break

    if guess in secret_fruit:
        update_clue(guess, secret_fruit, clue)
    else:
        print('Incorrect. You lose a chance.')
        Chances = Chances - 1

if guessed_fruit_correctly:
    print('You won! The secret fruit was ' + secret_fruit)
else:
    print('You lost! The secret fruit was ' + secret_fruit)
