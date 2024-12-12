import random
import hangman_words
import Hangman_arts

lives = 6

print(Hangman_arts.logo)

random_word = random.choice(hangman_words.word_list)
# print(random_word)

placeholder = " "
word_length = len(random_word)

for _ in range(0, word_length):
    placeholder += "_"
print(placeholder)   

game_over = False

correct_letters = []

while not game_over:
    print(" \n")
    print(f"***************************{lives}/6 LIVES LEFT*************************** \n")
    ask_letter = input("Guess a letter: ").lower()

    if ask_letter in correct_letters:
        print(f"You've already guessed {ask_letter}.")

    display = ""

    for letter in random_word:
        if letter == ask_letter:
            display += letter
            correct_letters.append(ask_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"    
            
    print(display)

    if ask_letter not in random_word:
        lives -= 1
        print(" \n")
        print(f"You guessed {ask_letter}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(" \n")
            print(f"***************************IT WAS '{random_word}'! YOU LOSE***************************")



    if  "_" not in display:
        game_over = True
        print(" \n")
        print("*****************************YOU WİN*****************************")



    print(Hangman_arts.stages[lives -1])