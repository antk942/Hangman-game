import Settings

mistakes = 0


def WordHandler(word, lettersFound, letter):
    givenWord = list(word)

    if not lettersFound:
        lettersFound = ["_"] * len(word)  # The first time create the lettersFound with the proper string.
    else:
        lettersFound = list(lettersFound)  # Or if it's not the first time, make the lettersFound string into a list.

    mar = LetterCheck(givenWord, lettersFound, letter)  # Check whether the letter is contained or not.
    if mar is not None:
        return "".join(mar), mistakes  # Return the previous lettersFound string if we had a mistake + mistakes.
    else:
        return "".join(lettersFound), mistakes  # Return the new lettersFound string + mistakes.


def LetterCheck(givenWord, lettersFound, letter):
    if not DuplicateCheck(letter):
        print("Give me a new letter.")
        return None

    global mistakes
    if letter not in givenWord:
        mistakes += 1  # Increase the number of mistakes the user had.
        return None

    for i in range(0, len(givenWord)):  # Check the locations of the letter given in the word.
        if givenWord[i] == letter:
            lettersFound[i] = letter[0]

    return lettersFound  # Return the new lettersFound string.


def DuplicateCheck(letter):
    if letter in Settings.alphabetList:
        Settings.alphabetList.remove(letter)
        return True
    else:
        return False
