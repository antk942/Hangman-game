import Settings

lines = []


def FillLines():
    global lines
    lines = [None] * Settings.verticalLen  # Make the lines list empty to handle the printing.


def PrintAll(hasMistakes, lettersFound):
    FillLines()  # Creating the lines list.
    AddHang()  # Adding the hanger.
    AddBody(hasMistakes)  # Adding the body parts.
    if lettersFound:  # If there are lettersFound add them.
        AddGuessed(lettersFound)

    for i in range(0, len(lines)):  # Print the lines as a final result.
        print(lines[i])


def AddHang():  # Adding the graphics of the hanger in the lines.
    lines[0] = Settings.hangLines["topLine"]
    lines[-1] = Settings.hangLines["botLine"]
    for i in range(1, Settings.verticalLen - 1):
        lines[i] = Settings.hangLines["verticalShape"]


def AddBody(mistakes):
    # Adding the graphics of the body in the lines depending on the mistakes made.
    emptyAmount = len(Settings.hangLines["topLine"]) - len(Settings.hangLines["verticalShape"])
    emptySpaces = (emptyAmount - 1) * " "  # Adding the empty space between the hanger graphics and the body graphics.
    bodyLen = 5

    if mistakes[0]:
        lines[1] += emptySpaces + Settings.bodyShapes["head"]
    if mistakes[1]:
        for i in range(2, bodyLen):
            lines[i] += emptySpaces + Settings.bodyShapes["torso"]
    if mistakes[2]:
        emptySpaces = emptySpaces[:-1]
        lines[3] = Settings.hangLines["verticalShape"] + emptySpaces + Settings.bodyShapes["hands"]
    if mistakes[3]:
        lines[bodyLen] += emptySpaces + Settings.bodyShapes["legs"]


def AddGuessed(lettersFound):  # Adding the guessed letters with an empty space between the word and the hanger.
    emptySpaces = Settings.wordEmptySpace * " "
    lines[6] += emptySpaces + lettersFound
