import string

global hangLines
hangLines = {
    "topLine": "     ─┰──────────┰",
    "verticalShape": "      │ ",
    "botLine": "──────┴──────"
}

global bodyShapes
bodyShapes = {
    "head": "▢",
    "torso": "┃",
    "leftLimb": "╱",
    "rightLimb": "╲"
}

global difficulty
difficulty = 6

global verticalLen
verticalLen = 10

global wordEmptySpace
wordEmptySpace = 25

global alphabetList
alphabetList = list(string.ascii_lowercase)