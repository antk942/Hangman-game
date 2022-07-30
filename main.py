import PrintFunctions
import WordHandler
import Play
import Settings


def DecidePlayer():
    while True:
        answer = input("Type 0 for AI or 1 for human: ")
        if not answer.isdigit() or int(answer) > 1:
            print("Please read the instructions.")
        else:
            return answer


if __name__ == '__main__':
    WordHandler.GetWordFromUser()
    # Print the first state where no mistakes have been made.
    PrintFunctions.PrintAll()

    Play.Play(DecidePlayer())





