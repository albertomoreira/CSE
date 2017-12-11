import random
num = random.randint(0,50)
print(num)


print("Guess a random number 0-50")
print("You have 5 guesses")

for x in range(5):
    guess = input("What is your guess bro?")

    if guess == str(num):
        print("Correct")
        quit()
    elif guess >= str(num):
        print("Lower")
    elif guess <= str(num):
        print("Higher")




































print("What is your name?")
input
print("Hello %s." % name)