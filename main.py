from fallout77.entity import Player
from fallout77.gamer import GameMaster

if __name__ == '__main__':

    player = Player(name=input("Name?"))
    game = GameMaster(player)
    game.welcum()

    while game.player.health:
        enemy = game.rand_enenmy()
        while enemy.health:
            game.fight_loop(enemy)



'''
TODO: 
Enemy Types
True-Bug
Farben fürs Terminal - Colorama
Refactoring
'''
