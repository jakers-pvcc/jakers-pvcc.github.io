# Name: Joshua Akers
# PORDLE

import random
wordlist = []
inFile = "animals.txt"
global wordFile

def main():
    global wordList
    wordFile = open(inFile, "r")
    for textLine in wordFile:
        for word in textLine.split():
            wordList.append(word)
    wordFile.close()

    playAgain = True
    while playAgain:
        printHeadings()
        playGame()
        yesno = input("Would you like to play again? (Y/N):  ")
        if yesno == "n" or yesno == "N":
            playAgain = False;
            print("Thank you for playing PORDLE!")
            return()

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you will try to guess the letters in the word.")
    print("Also, if you fail to guess the word, you will die within the next 24 hours.")
    print("The number of dashes indicates the number of letters in the word.")
    print("\nGet ready for a new word!")

def playGame():
    numGuesses = 1
    lettersUsed = []

    wordchosen = random.choice(wordList)
    pordle = wordchosen
    for i in range (len(pordle)):
        pordle = pordle[0:1] + "_" + pordle[i+1:]
    print (" ".join(pordle))

    while pordle != wordchosen:
        letterguess = input("Please enter a letter: ")
        letterguess = letterguess.lower()
        lettersUsed.append(letterguess)
        print ("Number of guesses: " + str(numGuesses))

        for i in range(len(wordchosen)):
            if wordchosen[i] == letterguess:
                pordle = pordle[0:i] + letterguess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle))
        numGuesses += 1

    print("Well done! You guessed in " + str(numGuesses-1) + " guesses!")

main()
