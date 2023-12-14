class Hangman:
  def __init__(word_list, num_lives = 5, self):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []
    
  def check_guess(guess).lower
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

    def ask_for_input():
    while True:
      guess = input("Enter a single letter")
      if not len(guess) == 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character.")
      elif guess in list_of_guesses:
        print("You already tried that letter!")
      else:
        print("Correct letter! Well done")
        check_guess(guess)
      
        list_of_guesses.append{guess}
