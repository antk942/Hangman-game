import PrintFunctions
import WordHandler

if __name__ == '__main__':
    word = "potato"
    while True:
        PrintFunctions.FillLines()
        PrintFunctions.PrintAll(True, True, True, True, "a_w_w___")
        letter = input("Give me a letter: ")
        if not letter.isalpha() or len(letter) > 1:
            print("dummy")
        else:
            WordHandler.WordHandler(word, letter)
