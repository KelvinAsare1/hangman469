class Hangman:
  def play_game(word_list):
    num_lives = 5
  def __init__(word_list, num_lives = 5, self):
    self.word = random.choice(word_list)
    self.word_guessed = ['_' for _ in self.word]
    self.num_letters = len(set(self.word))
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []
    
  def check_guess(guess):
    while True:
      guess = input("Enter a single letter")
      guess_lower = guess.lower()
      if len(guess) == 1 and guess.isalpha():
        print("Good Guess!")
        break
      else:
        print("Invalid letter. Please, enter a single alphabetical character.")
      if guess in word:
          print("Good Guess" guess, "is in the word")
          for letter in word:
            if letter == guess:
              idx = word.index(letter) 
              word_guessed[idx] = letter
          num_letters = num_letters -1
            
      else:
          print("Sorry" guess, "is not in the word. Try again.")
          num_lives = num_lives -1
          print("Sorry" + letter + "is not in the word.")
          print("You have" + num_lives + "lives left.")

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
