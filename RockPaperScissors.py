from random import randint

pWin = 0
pLoss = 0
pTie = 0

choices = ["Rock", "Paper", "Scissors"]

cChoice = choices[randint(0, 2)] # Determine computers choice

player = False # Set player to false to loop through while statement

while player == False:
    pChoice = input("Rock, Paper, or Scissors? ")
    print("")
    if pChoice == cChoice:
        pTie += 1
        print("You tied!", cChoice, "does nothing to", pChoice + "!")
        print("")
        print("Wins:", pWin)
        print("Losses:", pLoss)
        print("Ties:", pTie)
        print("")
    elif pChoice == "Rock":
        if cChoice == "Paper":
            pLoss += 1
            print("You lose!", cChoice, "covers", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
        else:
            pWin += 1
            print("You win!", cChoice, "is crushed by", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
    elif pChoice == "Paper":
        if cChoice == "Scissors":
            pLoss += 1
            print("You lose!", cChoice, "cuts", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
        else:
            pWin += 1
            print("You win!", cChoice, "covers", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
    elif pChoice == "Scissors":
        if cChoice == "Rock":
            pLoss += 1
            print("You lose!", cChoice, "crushes", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
        else:
            pWin += 1
            print("You win!", cChoice, "is cut by", pChoice + "!")
            print("")
            print("Wins:", pWin)
            print("Losses:", pLoss)
            print("Ties:", pTie)
            print("")
    else:
        print("Invalid input. Try again.")
        print("")
        print("Wins:", pWin)
        print("Losses:", pLoss)
        print("Ties:", pTie)
        print("")

    player = False # Set player to false to loop through while statement
    cChoice = choices[randint(0, 2)] # Determine computers choice