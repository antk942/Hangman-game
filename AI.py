import random

import Settings


def GetRandomLetter():
    letter = Settings.alphabetList[random.randrange(0, len(Settings.alphabetList))]
    print("Ai choose: " + letter)
    return letter


def GetWeightedLetter():
    weights = []
    alphabetLen = len(Settings.alphabetList)

    for i in range(alphabetLen):
        if i == 0:
            weights.append(100)
        else:
            weights.append(weights[i - 1] / 1.3)
    print(weights)

    return random.choices(Settings.alphabetList, weights=tuple(weights), k=1)[0]

