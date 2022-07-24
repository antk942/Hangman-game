import PrintFunctions
import WordHandler


def GetWordFromUser():  # Get a word from the user and return it, checking that it only contains letters.
    while True:
        wordGiven = input("Give me a word you want to guess: ")
        if not wordGiven.isalpha():
            print("Please read the instructions.")
        else:
            return wordGiven.lower()


def WinSituation():  # Print the winning screen with the word completed and the current state of mistakes.
    PrintFunctions.PrintAll(mistakes, word.lower())
    print("GG")


def MistakesSituation(mistakesMade):
    for i in range(0, mistakesMade):
        mistakes[i] = True


def MainRun(letsFound):
    while True:
        userInput = input("Give me a letter or a guessed word: ")
        if not userInput.isalpha():  # Check if the letter or word contains something other than letters.
            print("Dummy, try to give me a letter or a guessed word.")
            continue

        # If the user gave a word, check if it's the correct one and print the proper response.
        if len(userInput) > 1:
            if word.lower() != userInput.lower():
                print("Wrong")
                continue
            else:
                WinSituation()
                break

        # If the user gives a letter check if it's contained in the word.
        rets = WordHandler.WordHandler(word.lower(), letsFound, userInput.lower())
        letsFound = rets[0]
        # Get the mistakes of the user until now.
        mistakesMade = rets[1]
        MistakesSituation(mistakesMade)

        # Check if all the letters have been found to print the winning state.
        if letsFound == word.lower():
            WinSituation()
            break

        # Print the next state with mistakes and the letters found until now.
        PrintFunctions.PrintAll(mistakes, letsFound)

        # Check if the user lost.
        if mistakesMade > 3:
            print("You lost :(")
            break


if __name__ == '__main__':
    mistakes = [False] * 4
    word = GetWordFromUser()
    # Print the first state where no mistakes have been made.
    PrintFunctions.PrintAll(mistakes, "_" * len(word))

    lettersFound = []

    MainRun(lettersFound)




