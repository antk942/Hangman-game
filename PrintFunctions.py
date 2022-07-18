import Settings

hangLines = Settings.hangLines
bodyShapes = Settings.bodyShapes
invisibleChar = "\u200b"

lines = []

verticalLen = Settings.verticalLen


def FillLines():
    for i in range(0, verticalLen):
        lines.append(invisibleChar)


def PrintAll():
    AddHang()
    AddBody(True, True, True, True)
    for i in range(0, len(lines)):
        print(lines[i])


def AddHang(topLine=hangLines["topLine"], verticalShape=hangLines["verticalShape"], botLine=hangLines["botLine"]):
    lines[0] = topLine
    lines[-1] = botLine
    for i in range(1, verticalLen - 1):
        lines[i] = verticalShape


def AddBody(head=False, torso=False, hands=False, legs=False):
    emptyAmount = len(hangLines["topLine"]) - len(hangLines["verticalShape"]) - 1
    emptySpaces = ""
    for i in range(0, emptyAmount):
        emptySpaces += " "
    if head:
        lines[1] += emptySpaces + bodyShapes["head"]
    if torso:
        for i in range(2, 5):
            lines[i] += emptySpaces + bodyShapes["torso"]
    if hands:
        emptySpaces = emptySpaces[:-1]
        lines[3] = hangLines["verticalShape"] + emptySpaces + bodyShapes["hands"]
    if legs:
        lines[5] += emptySpaces + bodyShapes["legs"]

