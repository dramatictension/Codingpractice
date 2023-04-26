import random
import hm_words

chosenword = random.choice(hm_words.word_list)
word_length = len(chosenword)
lives = 6


print(f"The chosen word is: {chosenword} , {word_length}")

display = []
for _ in chosenword:
    display += "_"
print(display)

while "_" in display and lives > 0:

    guess = input("Choose a letter: ").lower()
    for position in range(word_length):
            letter = chosenword[position]
            if letter == guess:
                display[position] = letter
    print(display)

    if guess not in chosenword:
         lives -= 1
         print(f"Sorry, wrong guess. {lives} lives left.")
         

if lives == 0:
    print("Sorry, no more lives. Game over!")
    print(display)
if "_" not in display and lives > 0:
     print("You win!! Congrats")