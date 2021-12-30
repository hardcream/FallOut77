import random
from .entity import ENEMIES, Entity
from typing import Type


class GameMaster:
    player_text = "Player attacks!"
    enemy_text = "Enemy attacks!"

    def __init__(self, player):
        self.player = player

    def welcum(self):
        print(f"Health: {self.player.health}\n"
              f"Your mission is clear!\n"
              f"Happy hunting {self.player.name}")

    def fight_loop(self):
        enemy = self.enemy_roll()
        attack_roll = random.randint(0, 1)
        while self.player.health > 0:
            if enemy.health <= 0:
                enemy = self.enemy_roll()
                attack_roll = random.randint(0, 1)
            if attack_roll:
                self.player_strike(enemy)
                self.enemy_strike(enemy)
            else:
                self.enemy_strike(enemy)
                self.player_strike(enemy)
        return

    def enemy_roll(self):
        x = random.randint(0, len(ENEMIES) - 1)
        enemy_type: Type[Entity] = ENEMIES[x]
        enemy = enemy_type()
        print(f"You fight a: {enemy.__class__.__name__}")
        return enemy

    def player_strike(self, enemy: Entity):
        player_attack = self.player.attack
        print("----------------"
              f"|{self.player.name} attacks with: {player_attack} |"
              "----------------")
        input()
        enemy.health = enemy.health - player_attack
        print(f"{enemy.__class__.__name__} Health: {enemy.health}")
        self.debug_health(enemy)
        return

    def enemy_strike(self, enemy: Entity):
        enemy_attack = enemy.attack
        print("----------------"
              f"|{enemy.__class__.__name__} attacks with: {enemy_attack} |"
              "----------------")
        input()
        self.player.health = self.player.health - enemy_attack
        print(f"{self.player.name} Health: {self.player.health}")
        self.debug_health(enemy)
        return

    def debug_health(self, enemy: Entity):
        print(f"DEBUG: Player = {self.player.health}")
        print(f"DEBUG: Enemy = {enemy.health}\n")
        return
