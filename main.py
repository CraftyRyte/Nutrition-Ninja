import pygame as pyg
import random


# Classes
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choices(['u', 'h'], weights=[0.3, .7])
        self.color = ''
        self.vel = 2
        self.rect = pyg.Rect(x, y, 20, 20)
        if self.type == ['u']:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

    def draw(self):
        self.rect = pyg.Rect(self.x, self.y, 20, 20)
        pyg.draw.ellipse(screen, self.color, self.rect)

    def grav(self):
        self.y += self.vel
        self.vel += 0.5

    def update(self):
        self.grav()
        self.draw()


# Window
dimensions = [600, 800]
screen = pyg.display.set_mode(tuple(dimensions))
pyg.display.set_caption("Health Ninja")

# Game loop and vars
clock = pyg.time.Clock()
is_running = True
spawn_rate = 1
spawn_time = 0
fruits = [Fruit(300, -20)]

while is_running:
    clock.tick(30)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False
    screen.fill((200, 157, 124))

    # spawning mech
    if pyg.time.get_ticks() > spawn_time:
        rand_pos = (random.randint(20, dimensions[0] - 20), -20)
        fruits.append(Fruit(rand_pos[0], rand_pos[1]))
        spawn_time += spawn_rate * 1000
        spawn_rate -= 0.01
    for i in fruits:
        if i.y > dimensions[1]:
            fruits.remove(i)
            del i
            continue
        i.update()
        # print(fruits)

    pyg.display.update()

pyg.quit()
exit()
