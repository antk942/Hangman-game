global mistakes
mistakes = 0


def WordHandler(word, lettersFound, letter):
    givenWord = list(word)

    if not lettersFound:
        lettersFound = ["_"] * len(word)
    else:
        lettersFound = list(lettersFound)

    mar = LetterCheck(givenWord, lettersFound, letter)
    if mar is not None:
        return "".join(mar)
    else:
        return "".join(lettersFound)


def LetterCheck(givenWord, lettersFound, letter):
    global mistakes
    if letter not in givenWord:
        mistakes += 1
        return None

    for i in range(0, len(givenWord)):
        if givenWord[i] == letter:
            lettersFound[i] = letter[0]

    return lettersFound


