import os
from tabulate import tabulate
from googletrans import Translator


class Simple_Translator(object):
    #comment
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.translator = Translator()

    def translation(self):
        translation = self.translator.translate(self.word, dest=self.language)
        data = [
            ["Original Sentence:", "Translated Sentence"],
            [self.word, str(translation.text)],
        ]
        return tabulate(data, headers="firstrow", tablefmt="fancy_grid")

    def __str__(self):
        return self.translation()


if __name__ == "__main__":
    sentence = input("Enter string to tabuate >> ")
    os.system("cls")
    print(Simple_Translator(sentence, "en"))
