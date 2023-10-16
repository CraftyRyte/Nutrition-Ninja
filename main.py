import pygame as pyg
import random


# Classes
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choices(["u", "h"])
        self.color = ''
        self.rect = pyg.Rect(x, y, 20, 20)
        if self.type == ['u']:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

    def draw(self):
        pyg.draw.ellipse(screen, self.color, self.rect)

    def update(self):
        self.draw()


# Window
dimensions = [600, 800]
screen = pyg.display.set_mode(tuple(dimensions))
pyg.display.set_caption("Health Ninja")

# Game loop and vars
clock = pyg.time.Clock()
is_running = True
fruit = Fruit(300, 300)

while is_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False
    screen.fill((200, 157, 124))
    fruit.draw()
    pyg.display.update()

pyg.quit()
exit()
