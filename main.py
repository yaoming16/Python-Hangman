import random
import hangman_art
from hangman_words import word_list

# at the end the player is asked if he wants to keep playing. As long as play is true you keep playing. If the player says "y" when the game ends, play will be true 
play = True
while play == True:
  print(hangman_art.logo)
  
  display = []
  word_number = random.randint(0,len(word_list) - 1)
  word = word_list[word_number]
  word_len = len(word)

  # for each letter of the word it creates a "_" space 
  for letter in word:
    display += "_"

  game = True
  lives = 6
  while game:
    guess = input("Enter a letter: ").lower()

    # If the guessed word is already guessed you get a message
    if guess in display: 
      print(f'\n{guess.upper()} was already guessed')

    for position in range(0, word_len):
      if word[position] == guess:
        display[position] = word[position]
        
    # if the guessed word is not correct you lose a life
    if guess not in word:
        lives -= 1
        print(f'\n{guess.upper()} is not in the word, you lose a life.\n ')
  
    print(hangman_art.stages[lives])
    print(f'{" ".join(display)}\n')

    # Lives are 0 so you lose
    if lives == 0:
      game = False
      print("You Lose")
      print(f'The word was: {word}\n')
      again = input("Do you wish to play again? Type y/n")
      if again == "y":
        play = True
      else:
        play = False

    # great you won !!
    if "_" not  in display:
      game = False
      print("You Won")
      if again == "y":
        play = True
      else:
        play = False