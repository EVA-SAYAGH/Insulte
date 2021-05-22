from printer import print_with_color

class Player:
    def __init__(self, name, weakness):
        self.name = name
        self.weakness = weakness
        self.score = 0
        self.current_insult = []
        self.current_insult_text = ''
        self.opponent_weakness = None

    def set_opponent_weakness(self, weakness):
        self.opponent_weakness = weakness

    def describe(self):
        return 'Player {} with weakness {}'.format(self.name, self.weakness)

    def play(self, words):
        print('Current score={}'.format(self.score))
        print('Current insult={}'.format(self.current_insult_text))
        print_with_color(
            'What action to choose ?\n1. Add words to your insult.\n2. Insult your opponent.\n3. Skip turn',
            color='yellow'
        )
        choice = input()
        if choice == '1':
            return self.choose_word(words)
        if choice == '2':
            self.terminate_insult()
            return 'TERMINATE INSULT'
        if choice == '3':
            return 'SKIP TURN'
        else:
            print_with_color('Could not understand your choice. Please enter an integer from 1 to 2.', color='red')
            return self.play(words)

    def choose_word(self, words):
        print('Possible words (choose index)')
        for index, word in enumerate(words, 1):
            print('\t{}. {}'.format(index, word.describe()))
        choice = input()
        try:
            choice_index = int(choice) - 1
        except ValueError:
            print_with_color('Could not understand your choice. Please enter an integer from 1 to {}.'.format(len(words)), color='red')
            return self.choose_word(words)
        if not 0 <= choice_index <= len(words) - 1:
            print_with_color('Could not understand your choice. Please enter an integer from 1 to {}.'.format(len(words)), color='red')
            return self.play(words)
        word_choosen = words.pop(choice_index)
        self.current_insult.append(word_choosen)
        self.current_insult_text += '{} '.format(word_choosen.text)
        return words

    def terminate_insult(self):
        print('{} says {} !'.format(self.name, self.current_insult_text))

        score = 0
        number_of_opponent_weakness_words = 0
        for word in self.current_insult:
            score += word.power
            if word.theme == self.opponent_weakness:
                number_of_opponent_weakness_words += 1
        if number_of_opponent_weakness_words / len(self.current_insult) > 0.3:
            print('Insult deals with the opponent weakness ! score is doubled.')
            score *=2
        if self.current_insult and (
                        self.current_insult[0].type == 'liaison' or
                        self.current_insult[-1].type == 'liaison'
        ):
            print_with_color('Bad syntax ! Score is divided by 3 !', color='red')
            score /= 3
        print_with_color('Score of the insult: {}'.format(score), color='yellow')
        self.score += score
        self.current_insult = []


PLAYERS = {
    'loic': Player('loic', "coding"),
    'eva': Player('eva', "weight"),
    'benjamin': Player('benjamin', "familly"),
}
