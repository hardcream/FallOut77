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
                self.enemy_strike(enemy)
                self.player_strike(enemy)
        else:
            while self.player.health > 0 and enemy.health > 0:
                self.player_strike(enemy)
                self.enemy_strike(enemy)

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
        player_attack = self.player.attack
        print("----------------"
              f"|{self.player.name} attacks with: {player_attack} |"
              "----------------")
        input()
        enemy.health = enemy.health - player_attack
        print(enemy.__class__.__name__, "Health: ", enemy.health)

        return

    def enemy_strike(self, enemy: Entity):
        enemy_attack = enemy.attack
        print("----------------"
              f"|{enemy.__class__.__name__} attacks with: {enemy_attack} |"
              "----------------")
        input()
        self.player.health = self.player.health - enemy_attack
        print(self.player.name, "Health: ", self.player.health)

        return

