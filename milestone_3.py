def check_guess(guess).lower

def ask_for_input():
    while True:
      guess = input("Enter a single letter")
      if len(guess) == 1 and guess.isalpha():
        print("Good Guess!")
        break
      else:
        print("Invalid letter. Please, enter a single alphabetical character.")
      if guess in word:
          print("Good Guess" guess, "is in the word")
      else:
          print("Sorry" guess, "is not in the word. Try again.")

  ask_for_input()
