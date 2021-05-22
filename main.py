from player import PLAYERS
from game import Game
from printer import print_with_color


def main():
    player1, player2 = choose_players()
    game = Game(player1, player2)
    game.run()

def choose_players():
    print_with_color('Available players:', color='green')
    for player in PLAYERS.values():
        print('\t' + player.describe())
    print_with_color('Player 1 : enter the name of you player', color='yellow')
    player1_name = input().lower()
    if player1_name not in PLAYERS:
        while player1_name.lower() not in PLAYERS:
            print_with_color('Unknow player {}! Enter a good name'.format(player1_name), color='red')
            player1_name = input().lower()
    print_with_color('Player 2 : enter the name of you player (not the same as player 1)', color='yellow')
    player2_name = input().lower()
    if player2_name not in PLAYERS or player2_name == player1_name:
        while player2_name not in PLAYERS or player2_name == player1_name:
            if player2_name not in PLAYERS:
                print_with_color(
                    'Unknow player {}! Enter a good name and no the same as player 1'.format(player2_name),
                    color='red'
                )
            else:
                print_with_color(
                    'You cannot choose this player name. Player 1 took it already !. Enter another player name',
                    color='red'
                )
            player2_name = input().lower()
    return PLAYERS[player1_name], PLAYERS[player2_name]


if __name__ == '__main__':
    main()
