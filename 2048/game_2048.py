"""2048 console game written in Python 3.10.12"""

import sys
import os

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
                self.display_playing_field()
            case Key.left:
                self.display_playing_field()
            case Key.up:
                self.display_playing_field()
            case Key.down:
                self.display_playing_field()
            case Key.esc:
                self.display_playing_field()
                sys.exit()
            case Key.enter:
                print("Game started/restarted")
                self.create_playing_field()
                self.display_playing_field()

    def display_playing_field(self):
        """TODO: Write display_playing_field() docstring"""
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in self.playing_board:
            print(row, end='\n')
        print()
        print("Use arrows to play.")
        print("Press 'ESC' to quit.")
        print("Press 'ENTER' to restart the game.")

    def start_game_loop(self):
        """TODO: Write start_game() docstring"""
        os.system('cls' if os.name == 'nt' else 'clear')
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
        self.playing_board = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

if __name__ == "__main__":
    game = Game2048()
    game.start_game_loop()
    