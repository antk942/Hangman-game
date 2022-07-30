import Settings


def GetWordFromUser():  # Get a word from the user and return it, checking that it only contains letters.
    while True:
        wordGiven = input("Give me a word that exists: ")

        if not wordGiven.isalpha():
            print("Please read the instructions.")
        else:
            Settings.word = wordGiven.lower()
            break


def WordHandler(word, lettersFound, letter):
    givenWord = list(word)

    if not lettersFound:
        lettersFound = ["_"] * len(word)  # The first time create the lettersFound with the proper string.
    else:
        lettersFound = list(lettersFound)  # Or if it's not the first time, make the lettersFound string into a list.

    LetterCheck(givenWord, lettersFound, letter)  # Check whether the letter is contained or not.


def LetterCheck(givenWord, lettersFound, letter):
    if not DuplicateLetterCheck(letter):
        print("Give me a new letter.")
        return None

    if letter not in givenWord:
        Settings.mistakes += 1  # Increase the number of mistakes the user had.
        return None

    for i in range(0, len(givenWord)):  # Check the locations of the letter given in the word.
        if givenWord[i] == letter:
            lettersFound[i] = letter[0]

    Settings.lettersFound = lettersFound  # Return the new lettersFound string.


def WordCheck(word):
    if not DuplicateWordCheck(word):
        Settings.mistakes += 1
    else:
        print("Give me a new word.")


def DuplicateLetterCheck(letter):
    if letter in Settings.alphabetList:
        Settings.alphabetList.remove(letter)
        return True
    else:
        return False


def DuplicateWordCheck(word):
    if word in Settings.guessedWords:
        return True
    else:
        Settings.guessedWords.append(word)
        return False
