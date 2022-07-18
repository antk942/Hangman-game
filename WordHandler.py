mistakes = 0


def WordHandler(word, letter):
    LetterCheck(word, letter)
    print(mistakes)


def LetterCheck(word, letter):
    global mistakes
    if letter.lower() not in word.lower():
        mistakes += 1
    else:
        print("moce")


