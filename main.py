from fallout77.entity import Player
from fallout77.gamer import GameMaster
import sys

if __name__ == '__main__':

    player = Player(name=input("Name?\n"))
    game = GameMaster(player)
    game.welcum()

    while game.player.health > 0:
        enemy = game.rand_enemy()
        while enemy.health > 0:
            game.fight_loop(enemy)
    sys.exit(0)

'''
TODO: 
Enemy Types
True-Bug
Farben fürs Terminal - Colorama
Refactoring
'''
