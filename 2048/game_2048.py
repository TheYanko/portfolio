"""2048 console game written in Python 3.10.12"""

import sys

from pynput import keyboard
from pynput.keyboard import Key

class Game2048():
    """TODO: Class docstring"""

    def __init__(self):
        self.playing_board = []

    def actions_on_key_release(self, key):
        """TODO: actions_on_key_release docstring"""
        match key:
            case Key.right:
                print("Right arrow pressed.")
            case Key.left:
                print("Left arrow pressed.")
            case Key.up:
                print("Up arrow pressed.")
            case Key.down:
                print("Down arrow pressed.")
            case Key.esc:
                print("Thanks for playing")
                sys.exit()
            case Key.enter:
                print("Game started/restarted")
                self.create_playing_field()


    def start_game_loop(self):
        """TODO: Write start_game() docstring"""
        print("Welcome to 2048 console game.")
        print("Made by Maciej Jankowski")
        print("Press 'Enter' to start/restart the game!")
        print("Press 'Esc' to exit.")
        print("Press arrows to play.")
        print()

        #Initialize keyboard monitoring with pynput
        with keyboard.Listener(on_release=self.actions_on_key_release) as listener:
            listener.join()

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
    