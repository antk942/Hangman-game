import random

import Settings


def GetRandomLetter():
    letter = Settings.alphabetList[random.randrange(0, len(Settings.alphabetList))]
    print("Ai choose: " + letter)
    return letter
