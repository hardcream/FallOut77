import random
from .entity import ENEMIES, Entity
from typing import Type


class GameMaster:
    player_text = "Player attacks!"
    enemy_text = "Enemy attacks!"

    def __init__(self, player):
        self.player = player

    def rand_enemy(self):
        x = random.randint(0, len(ENEMIES) - 1)
        enemy_type: Type[Entity] = ENEMIES[x]
        enemy = enemy_type()
        return enemy

    def welcum(self):
        print(f"Health: {self.player.health}\n"
              f"Your mission is clear!\n"
              f"Happy hunting {self.player.name}")

    def fight_loop(self, enemy: Entity):
        x = self.first_strike()
        if x:
            while self.player.health > 0 and enemy.health > 0:
                self.enemy_strike(enemy)
                if self.player.health > 0:
                    self.player_strike(enemy)
            print(f"{self.player.name} died.")
        else:
            while self.player.health > 0 and enemy.health > 0:
                self.player_strike(enemy)
                if enemy.health > 0:
                    self.enemy_strike(enemy)
                if enemy.health <= 0:
                    print(f"{enemy.__class__.__name__} died.")
                    continue
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
        self.debug_health(enemy)
        return

    def enemy_strike(self, enemy: Entity):
        enemy_attack = enemy.attack
        print("----------------"
              f"|{enemy.__class__.__name__} attacks with: {enemy_attack} |"
              "----------------")
        input()
        self.player.health = self.player.health - enemy_attack
        print(self.player.name, "Health: ", self.player.health)
        self.debug_health(enemy)
        return

    def debug_health(self, enemy: Entity):
        print(f"DEBUG: Player = {self.player.health}")
        print(f"DEBUG: Enemy = {enemy.health}")
