"""2048 console game written in Python 3.10.12"""

import sys
import os
import random

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
        row1, row2, column1, column2 = 0, 0, 0, 0
        
        #Generating two random spots coordination for beginning numbers
        while row1 == row2 and column1 == column2:
            row1 = random.randint(0, 3)
            row2 = random.randint(0, 3)
            column1 = random.randint(0, 3)
            column2 = random.randint(0, 3)

        #Placing two starting 2 on a board
        self.playing_board[row1][column1] = 2
        self.playing_board[row2][column2] = 2

if __name__ == "__main__":
    game = Game2048()
    game.start_game_loop()
    