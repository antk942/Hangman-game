import Settings

lines = []


def FillLines():
    global lines
    lines = [None] * Settings.verticalLen


def PrintAll(hasHead, hasTorso, hasHands, hasLegs, lettersFound):
    FillLines()
    AddHang()
    AddBody(hasHead, hasTorso, hasHands, hasLegs)
    if lettersFound:
        AddGuessed(lettersFound)

    for i in range(0, len(lines)):
        print(lines[i])


def AddHang():
    lines[0] = Settings.hangLines["topLine"]
    lines[-1] = Settings.hangLines["botLine"]
    for i in range(1, Settings.verticalLen - 1):
        lines[i] = Settings.hangLines["verticalShape"]


def AddBody(hasHead=False, hasTorso=False, hasHands=False, hasLegs=False):
    emptyAmount = len(Settings.hangLines["topLine"]) - len(Settings.hangLines["verticalShape"])
    emptySpaces = (emptyAmount - 1) * " "
    bodyLen = 5

    if hasHead:
        lines[1] += emptySpaces + Settings.bodyShapes["head"]
    if hasTorso:
        for i in range(2, bodyLen):
            lines[i] += emptySpaces + Settings.bodyShapes["torso"]
    if hasHands:
        emptySpaces = emptySpaces[:-1]
        lines[3] = Settings.hangLines["verticalShape"] + emptySpaces + Settings.bodyShapes["hands"]
    if hasLegs:
        lines[bodyLen] += emptySpaces + Settings.bodyShapes["legs"]


def AddGuessed(lettersFound):
    emptySpaces = Settings.wordEmptySpace * " "
    lines[6] += emptySpaces + lettersFound
