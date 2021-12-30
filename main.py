import sys

from fallout77.entity import Player
from fallout77.gamer import GameMaster

if __name__ == '__main__':

    player = Player(name=input("Name?\n"))
    game = GameMaster(player)
    game.welcum()
    game.fight_loop()
    sys.exit(0)

'''
TODO: 
Enemy Types
True-Bug
Farben fürs Terminal - Colorama
Refactoring
'''
