import sys

class MorseTranslater:
    def __init__(self, input: str):
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
