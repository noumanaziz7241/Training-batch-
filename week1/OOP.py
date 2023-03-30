#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:55:03 2023

@author: nouman
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self):
        dice = random.randint(1, 6)
        if dice % 2 == 0:
            self.score = 2 * dice
        else:
            self.score = dice

        coin = random.choice(['Head', 'Tail'])
        if coin == 'Head':
            self.score *= 3
        else:
            self.score -= 1

        print(f"{self.name} scored {self.score} ({dice}, {coin})")

def play_game(p1, p2):
    p1.play()
    p2.play()
    if p1.score > p2.score:
        return p1
    else:
        return p2

# Initialize the players
player1 = Player(input('Enter name of Player 1: '))
player2 = Player(input('Enter name of Player 2: '))
player3= Player(input('Enter name of Player 3: '))
player4= Player(input('Enter name of Player 4: '))


# Play game 1
print("Playing Game 1")
winner1 = play_game(player1, player2)

# Play game 2
print("Playing Game 2")
winner2 = play_game(player3, player4)

# Play the final game
print("Playing the Final Game")
finalist1 = winner1
finalist2= winner2
winner = play_game(finalist1, finalist2)

# Print the winner
print(f"{winner.name} wins with a score of {winner.score}")

