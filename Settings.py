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
alphabetList = ["e", "i", "a", "n", "o", "r", "s", "t", "l", "c", "u", "d", "p", "m", "h", "g", "y", "b", "f", "v", "k", "w", "z", "x", "q", "j"]
# list(string.ascii_lowercase)

global guessedWords
guessedWords = []

global lettersFound
lettersFound = []

global mistakes
mistakes = 0

global word
word = ""

