import PrintFunctions
import WordHandler


def GetWordFromUser():
    while True:
        wordGiven = input("Give me a word you want to guess: ")
        if not wordGiven.isalpha():
            print("Please read the instructions.")
        else:
            return wordGiven.lower()


if __name__ == '__main__':
    mistakes = [False] * 4
    word = GetWordFromUser()
    PrintFunctions.PrintAll(mistakes[0], mistakes[1], mistakes[2], mistakes[3], "_" * len(word))

    lettersFound = []

    while True:

        userInput = input("Give me a letter or a guessed word: ")

        if not userInput.isalpha():
            print("Dummy, try to give me a letter or a guessed word.")
            continue

        if len(userInput) > 1:
            if word.lower() != userInput.lower():
                print("Wrong")
                continue
            else:
                print("GG")
                break

        lettersFound = WordHandler.WordHandler(word.lower(), lettersFound, userInput.lower())

        if lettersFound == word.lower():
            print("GG")
            break

        PrintFunctions.PrintAll(mistakes[0], mistakes[1], mistakes[2], mistakes[3], lettersFound)


