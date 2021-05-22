from dictionnary import Dictionnary
from printer import print_with_color

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_to_play = True
        self.last_player_skip = False
        self.end_of_game = False
        self.player1.set_opponent_weakness(player2.weakness)
        self.player2.set_opponent_weakness(player1.weakness)
        dictionnary = Dictionnary()
        self.words = dictionnary.get_words()

    def ask_player_to_play(self):
        if self.player1_to_play:
            player = self.player1
        else:
            player = self.player2
        print_with_color('player {} to play'.format(player.name), color="blue")
        player_output = player.play(self.words)
        if player_output =='TERMINATE INSULT':
            self.last_player_skip = False
        elif player_output == 'SKIP TURN':
            if self.last_player_skip:
                print_with_color('Both Player skipped that round. End of game', color="blue")
                self.end_of_game = True
            else:
                self.last_player_skip = True
        else:
            self.last_player_skip = False
            self.words = player_output


        self.player1_to_play = not self.player1_to_play

    def run(self):
        while len(self.words) > 0 and not self.end_of_game:
            self.ask_player_to_play()
        score1 = self.player1.score
        score2 = self.player2.score
        if score1 == score2:
            print_with_color('It is a draw ! Everyone has {} points.'.format(score1), color='yellow')
        elif score1 > score2:
            print_with_color('{} wins with {} points.'.format(self.player1.name, score1), color='green')
            print_with_color('{} looses with {} points.'.format(self.player2.name, score2), color='red')
        else:
            print_with_color('{} wins with {} points.'.format(self.player2.name, score2), color='green')
            print_with_color('{} looses with {} points.'.format(self.player1.name, score1), color='red')
