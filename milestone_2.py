import random
def choose_word():
    word_list = ['watermelon', 'banana', 'orange', 'mango', 'grapes']
    return random.choice(word_list)
word = choose_word()
guess = input("Enter a single letter")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print"(Oops! That is not a valid input.")
