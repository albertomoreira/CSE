import random
import string


"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick random item from the list
3. Hide the word (use *)
4. Reveal letters already guessed
5. Create the win conditions

"""
guesses_left = 10
word_bank = ["YoU lOsE", " Im the swinger for the LA Lakers", "apple", "superman", "spiderman", "boxing",
             "skateboard", "adidas", "supreme", "bape"]
random_word = word_bank[random.randint(0, len(word_bank) - 1)]
letters_guessed = []

while guesses_left:
    # Generate the output
    output = []
    for letter in random_word:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))

    # Check for win
    if '*' not in output:
        print("YOU WIN!!!!!")
        break

    current_guess = input("Type a letter: ").lower()
    letters_guessed.append(current_guess)
    print(letters_guessed)


    # Lose
    if current_guess not in random_word:
        guesses_left -= 1
    print(guesses_left)




