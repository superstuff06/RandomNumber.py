import random
answer = random.randint(0,100)
print("Lets Play a Guessing Game!!!")
print("I'm thinking of a number from 1 to 100")
playAgain = ""
amountGuess = 0
while playAgain != ("no"):
    urGuess = input("What is my number?: ")
    urGuess = int(urGuess)
    if urGuess == answer:
        amountGuess = amountGuess + 1
        print("Yay you got it!!!")
        print("You got it in " + str(amountGuess) + " guesses!")
        while playAgain != "yes" or "no" :
          playAgain = input("Play Again?: ")
          playAgain.lower()
          print(playAgain)
          if playAgain == ("yes"):
            amountGuess = 0
            answer = random.randint(0,100)
            print(playAgain)
            break
          elif playAgain == ("no"):
            break
          else:
            print("Please type either yes or no...")
    elif urGuess < answer:
        print("Nope thats too low :0")
        amountGuess = amountGuess + 1
    elif urGuess == 6969:
        print(answer)
    elif urGuess > answer:
        print("Nope thats too high :0")
        amountGuess = amountGuess + 1
