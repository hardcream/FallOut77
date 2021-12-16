import random
from .entity import ENEMIES, Entity
from typing import Type


class GameMaster:
    player_text = "Player attacks!"
    enemy_text = "Enemy attacks!"

    def __init__(self, player):
        self.player = player

    def rand_enenmy(self):
        x = random.randint(0, len(ENEMIES) - 1)
        enemy_type: Type[Entity] = ENEMIES[x]
        enemy = enemy_type()
        return enemy

    def welcum(self):
        print("Help, maybe? ")

    def fight_loop(self, enemy: Entity):
        x = self.first_strike()
        if x:
            while self.player.health > 0 and enemy.health > 0:
                self.player_strike(enemy)
                self.enemy_strike(enemy)
        else:
            while self.player.health > 0 and enemy.health > 0:
            self.enemy_strike(enemy)
            self.player_strike(enemy)

        return

    def first_strike(self):
        x = random.randint(0, 1)
        if x:
            print("---------------------"
                  "|Enemy attacks first|"
                  "---------------------")
        else:
            print("-----------------------"
                  f"| {self.player.name} attacks first |"
                  "-----------------------")

        return x

    def player_strike(self, enemy: Entity):
        print("----------------"
              f"|{self.player.name} attacks with: {self.player.attack} |"
              "----------------")
        input()
        enemy.health = enemy.health - self.player.attack
        self.player.health = self.player.health - enemy.attack
        print(enemy.__class__.__name__, "Health: ", enemy.health)

        return

    def enemy_strike(self, enemy: Entity):
        print("----------------"
              f"|{enemy.__class__.__name__} attacks with: {enemy.attack} |"
              "----------------")
        input()
        self.player.health = self.player.health - enemy.attack
        enemy.health = enemy.health - self.player.attack
        print(self.player.name, "Health: ", self.player.health)

        return

