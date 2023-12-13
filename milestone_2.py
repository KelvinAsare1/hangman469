import random
word_list = [watermelon, banana, orange, mango, grapes]
def choose_word():
    word_list = ['watermelon', 'banana', 'orange', 'mango', 'grapes']
    return random.choice(word_list)
word = random.choice(word_list)
guess = input("Enter a single letter")
if len(guess) = 1 and isalpha(guess),
    print("Good Guess!")
else:
    print"(Oops! That is not a valid input.")
