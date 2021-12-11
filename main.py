from fallout77.entity import Player, Enemy
import random


def flip_coin():
    return random.choice([True, False])


def attack_text_player():
    return input(f"---------------------\n"
                 f"Player attacks"
                 f"\n---------------------")


def attack_text_enemy():
    input(f"---------------------\n"
          f"Enemy attacks"
          f"\n---------------------")


if __name__ == '__main__':
    input("Press Enter to start the journey")

    player_health = 100
    player = Player(player_health)
    print(player)
    input("Start Fight")

    while player_health > 0:
        first_strike = flip_coin()
        if first_strike:
            input(first_strike)
            input(f"---------------------\n"
                  f"Player strikes first"
                  f"\n---------------------")
            enemy_health = 100
            enemy = Enemy(enemy_health)
            input(f"Enemy {enemy}\n")

            while player_health > 0 and enemy_health > 0:
                attack_text_player()
                player_attack = random.randint(1, 20)
                input(f"Player Attack: {player_attack}")
                enemy_health = enemy_health - player_attack
                input(f"Enemy Health: {enemy_health}\n")
                if enemy_health <= 0:
                    input("Yoooo, he dead bro :(\n"
                          "Press F to pay respect")
                else:
                    attack_text_enemy()
                    enemy_attack = random.randint(1, 20)
                    input(f"Enemy Attack: {enemy_attack}")
                    player_health = player_health - enemy_attack
                    input(f"Player Health: {player_health}\n")
                    if player_health <= 0:
                        input("Yoooo, you dead bro :(\n"
                              "F was pressed")
        else:
            input("Enemy strikes first")
            enemy_health = 100
            enemy = Enemy(enemy_health)
            input(f"Enemy {enemy}\n")

            while player_health > 0 and enemy_health > 0:
                attack_text_player()
                player_attack = random.randint(1, 20)
                input(f"Player Attack: {player_attack}")
                enemy_health = enemy_health - player_attack
                input(f"Enemy Health: {enemy_health}\n")
                if enemy_health <= 0:
                    input("Yoooo, he dead bro :(\n"
                          "Press F to pay respect")
                else:
                    attack_text_enemy()
                    enemy_attack = random.randint(1, 20)
                    input(f"Enemy Attack: {enemy_attack}")
                    player_health = player_health - enemy_attack
                    input(f"Player Health: {player_health}\n")
                    if player_health <= 0:
                        input("Yoooo, you dead bro :(\n"
                              "F was pressed")
