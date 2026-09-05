from pgzero.actor import Actor
from config import WIDTH

class Bullet:
    def __init__(self, x, y, speed=12, image="bullets/laser_player"):
        self.speed = speed
        self.actor = Actor(image, (x, y))

    def move(self):
        self.actor.x += self.speed

    def is_off_screen(self):
        return self.actor.x > WIDTH + 20

    def draw(self):
        self.actor.draw()

class EnemyBullet(Bullet):
    def __init__(self, x, y, speed=8, image="bullets/laser_enemy"):
        super().__init__(x, y, speed, image)

    def move(self):
        self.actor.x -= self.speed

    def is_off_screen(self):
        return self.actor.x < -20
