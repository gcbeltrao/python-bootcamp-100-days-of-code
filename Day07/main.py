from replit import clear
import random
import word_list
import hangman_art

display = []
chosen_word = random.choice(word_list.word_list)
end_of_game = False
lives = 6

print(hangman_art.logo)

for letter in chosen_word:
  display.append("_")

while not end_of_game:
  guess = (input("Guess a letter\n")).lower()

  clear()
  
  if guess in display:
    print("You have already inserted this letter.")

      
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
       display[position] = letter
   

  
  if guess not in chosen_word:
     print(f"\nThe letter '{guess}' is not in the word")
     lives -= 1
     if lives == 0:
       end_of_game = True
       print("You lose")
       
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You win!")

  print(hangman_art.stages[lives])