from fallout77.entity import Player, Enemy
import random


def flip_coin():
    return random.choice([True,False])


if __name__ == '__main__':
    input("Press Enter to start the journey")

    player_health = 100
    player = Player(player_health)
    print(player)
    input("Start Fight")

    while player.health > 0:
        first_strike = flip_coin()
        if first_strike:
            print(first_strike)
            print("Player strikes first")
            enemy_health = 100
            enemy = Enemy(enemy_health)
            print(enemy)

            while player.health > 0 or enemy.health > 0:
                player_attack = random.randint(1, 20)
                enemy_health = enemy_health - player_attack
                print(enemy_health)
                if enemy_health <= 0:
                    print("Yoooo, he dead bro :(")
                else:
                    print("Enemy attacks")
                    enemy_attack = random.randint(1, 20)
                    player.health = player.health - enemy_attack
                    print(player_health)
        else:
            print("Enemy strikes first")
