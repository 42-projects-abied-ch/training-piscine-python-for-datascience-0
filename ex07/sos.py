import sys

class MorseTranslater:
    def __init__(self, input: str) -> None:
        self.input = input
        self.encoding = {
            " ": "/ ",
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
            "0": "----- ",
        }
    
    def translate(self) -> str:
        result = ""
        for c in self.input:
            if c.upper() in self.encoding:
                result += self.encoding[c.upper()]
            else:
                raise AssertionError("the arguments are bad")
        return result


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        translator = MorseTranslater(sys.argv[1])
        print(translator.translate())
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
