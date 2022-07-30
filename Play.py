import random

import WordHandler
import Settings
import PrintFunctions
import AI


def Play(decision):
    word = Settings.word
    while True:
        if decision == "0":
            userInput = AI.GetRandomLetter()
        else:
            userInput = input("Give me a letter or a guessed word: ")
            if not userInput.isalpha():  # Check if the letter or word contains something other than letters.
                print("Dummy, try to give me a letter or a guessed word.")
                continue
            userInput = userInput.lower()

        # If the user gave a word, check if it's the correct one and print the proper response.
        if len(userInput) > 1:
            if word != userInput:
                WordHandler.WordCheck(userInput)
                PrintFunctions.PrintAll()
                continue
            else:
                PrintFunctions.WinSituation()
                break

        # If the user gives a letter check if it's contained in the word.
        WordHandler.WordHandler(word, Settings.lettersFound, userInput)

        # Check if all the letters have been found to print the winning state.
        if Settings.lettersFound == word:
            PrintFunctions.WinSituation()
            break

        # Print the next state with mistakes and the letters found until now.
        PrintFunctions.PrintAll()

        # Check if the user lost.
        if Settings.mistakes > Settings.difficulty - 1:
            print("You lost :(")
            break
