import pdb

import pygame as pyg
import random


# Classes
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choices(['u', 'h'], weights=[0.3, 0.7])
        self.color = (0, 0, 0) if self.type == ['u'] else (255, 255, 255)
        self.rect = pyg.Rect(x, y, 20, 20)
        self.vel = 200  # Adjust this value for gravity strength

    def update(self, dt):
        self.y += self.vel * dt / 1000
        self.vel += 400 * dt / 1000  # Adjust this value for gravity strength
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pyg.draw.ellipse(screen, self.color, self.rect)


# Initialize Pygame
pyg.init()

# Window
dimensions = [300, 400]
screen = pyg.display.set_mode(tuple(dimensions), pyg.RESIZABLE)
pyg.display.set_caption("Health Ninja")

# Game loop and vars
clock = pyg.time.Clock()
is_running = True
spawn_rate = 1
spawn_time = 0
fruits = []

last_time = pyg.time.get_ticks()

while is_running:
    dim = pyg.display.get_window_size()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False

    screen.fill((200, 157, 124))

    # Calculate time passed since the last frame
    current_time = pyg.time.get_ticks()
    dt = current_time - last_time
    last_time = current_time

    # Spawning mechanism
    if current_time > spawn_time:
        rand_pos = (random.randint(20, dim[0] - 20), -20)
        fruits.append(Fruit(rand_pos[0], rand_pos[1]))
        spawn_time += spawn_rate * 1000
        if spawn_rate > 0.19:
            spawn_rate -= 0.1

    for i in fruits:
        if i.y > dim[1]:
            # pdb.set_trace()
            fruits.remove(i)
        else:
            i.update(dt)
            i.draw(screen)

    pyg.display.update()
pyg.quit()

