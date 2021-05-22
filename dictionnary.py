from constants import words


class Word:
    def __init__(self, text, type, theme, power):
        self.text = text
        self.type = type
        self.theme = theme
        self.power = power

    def describe(self):
        return '{}: theme={}, type={}, power={}'.format(
            self.text, self.theme, self.type, self.power
        )

class Dictionnary:
    def __init__(self):
        self.words = []
        for theme in words:
            for type in words[theme]:
                for word in words[theme][type]:
                    power = words[theme][type][word]
                    self.words.append(Word(word, type, theme, power))

    def get_words(self):
        return self.words
