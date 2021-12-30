import random


class Entity:
    health = 100
    attack_range = (10, 30)

    def __init__(self):
        self._attack = None

    @property
    def attack(self):
        return random.randint(*self.attack_range)

    def __repr__(self):
        return f"Health: {self.health}\n" \
               f"Attack: {self.attack}\n"

    def echo(self):
        print(self.health)
        print(self.attack)
        print(self.name)


class Player(Entity):
    attack_range = (40, 60)

    def __init__(self, name, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = name


class Spider(Entity):
    pass


class Skeleton(Entity):
    pass


ENEMIES = [Spider, Skeleton]

__all__ = ["Spider", "Player", "Skeleton", "ENEMIES"]
