"""2048 console game written in Python 3.10.12"""

class Game2048():
    """TODO: Class docstring"""

    def __init__(self):
        self.playing_board = []

    def start_game_loop(self):
        """TODO: Write start_game() docstring"""
        print("Welcome to 2048 console game.")
        print("Made by Maciej Jankowski")
        print("Press ''Enter'' to start the game!")
        print("Enter 'q' and press 'Enter' to exit.")
        print("Press arrows and press 'Enter' to play.")
        print()

        key_input = input()

        #Setting up the playing field
        self.create_playing_field()

        #Gamplay loop
        while key_input != 'q':
            key_input = input()

            match key_input:
                case 'q':
                    print("Thanks for playing!")

    def create_playing_field(self):
        """TODO: Write create_playing_field() docstring"""
        playing_board = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
        return playing_board

if __name__ == "__main__":
    game = Game2048()
    game.start_game_loop()
    