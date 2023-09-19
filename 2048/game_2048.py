"""2048 console game written in Python 3.10.12"""

class Game2048():
    """TODO: Class docstring"""

    def __init__(self):
        self.playing_board = []

    def start_game_loop(self):
        """TODO: Write start_game() docstring"""
        print("Welcome to 2048 console game.")
        print("Made by Maciej Jankowski")

    def create_playing_field(self):
        """TODO: Write create_playing_field() docstring"""
        playing_board = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
        return playing_board

if __name__ == "__main__":
    print("Hello World!")
    