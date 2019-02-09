from random import randint

print('''
Welcome to the Higher or Lower game!\n
The game works by having the computer generate a random number which you have to guess.\n
After every guess, you will be told if your guess was too high or too low.\n
Once you guess the number, the game is over!
''')

num = randint(1, 100)
userGuessed = []
userGuess = int(input("Guess the number! It is between 1 and 100: \n"))
userGuessed.append(userGuess)

while userGuess != num:
    if userGuess > num:
        print("Your guess was TOO HIGH!\n")
    elif userGuess < num:
        print("Your guess was TOO LOW!\n")
    userGuess = int(input("Guess the number! It is between 1 and 100: \n"))
    userGuessed.append(userGuess)
else:
    print("You guessed the number! Congratulations!\n")
    print("It took you %i guesses!\n" % len(userGuessed))
    print("You guessed these numbers: %s \n" % userGuessed)