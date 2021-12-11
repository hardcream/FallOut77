class Entity:
    def __init__(self, health):
        self.health = health
        self.attack = None
    def __repr__(self,):
        return f"Health: {self.health} \n" \
               f"Rolled Attack: {self.attack}"

    def echo(self):
        print(self.health)
        print(self.attack)


class Player(Entity):
    pass


class Enemy(Entity):
    pass

