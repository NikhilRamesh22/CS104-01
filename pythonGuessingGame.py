gameOver=False
import random
theComputerNumber = random.randint(1,1000000)
#print(theComputerNumber)
numberOfGuesses = 0
lowGuessRange = 1
highGuessRange = 1000000
while not gameOver:
    print ("Enter a guess in range from", lowGuessRange, "to", highGuessRange)
    playerGuess  = int(input("Enter your guess: "))
    if(playerGuess < lowGuessRange or playerGuess > highGuessRange):
        print ("Guess out of range, try again!")
        continue
    if playerGuess > theComputerNumber:
        highGuessRange = playerGuess
        numberOfGuesses = numberOfGuesses+1
        if numberOfGuesses is 20:
            print("Game over, you ran out of guesses!")
            gameOver = True
        else:
            print("The number is lower. You have guessed ",numberOfGuesses, "times.")
    if playerGuess < theComputerNumber:
        lowGuessRange = playerGuess
        numberOfGuesses = numberOfGuesses+1
        if numberOfGuesses is 20:
            print("Game over, you ran out of guesses!")
            gameOver = True
        else:
            print("the number is higher. You have guessed ",numberOfGuesses, "times.")
            continue
    if playerGuess == theComputerNumber:
        print ("congratulations! That's correct!")
        gameOver = True

        
    
    
    
