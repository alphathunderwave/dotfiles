#!/usr/bin/env python3

import pygame
import numpy as np
import time

def map(z , celi, new_celi):
    return int((z / float( celi ) ) *new_celi )

class Rain:
    def __init__(self):
        self.x = np.random.randint(0 , 5120)
        self.y = np.random.randint(-750 , -50)

        self.z = np.random.randint(0 , 100)

        self.len = map(self.z , 100 , 50)
        self.speed = map(self.z , 100 , 8)
        self.width = map(self.z , 100 , 3)

    def fall(self):
        self.y = self.y + self.speed
        if self.y > 1080:
            self.x = np.random.randint(0 , 5120)
            self.y= np.random.randint(-750 , -50)

screen = pygame.display.set_mode((5120, 1080))

running = 1

drops = []

backrounds_night = [(255,255,255),(230,231,233),(205,208,212),(180,185,191),(155,162,169),(130,139,148),
                (105,116,127),(80,93,105),(54,70,84),(29,47,63),(5,24,42),(4,21,37)]
backrounds = backrounds_night[::-1]

for b in backrounds_night:
    backrounds.append(b)

for i in range(6000):
    r = Rain()
    drops.append(r)

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    elif event.type == pygame.KEYDOWN:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN:
        running = 0

    screen.fill(backrounds[int(time.strftime("%H"))])

    for i in range(len(drops)):
        r=drops[i]
        pygame.draw.line(screen, (56, 147, 177), (r.x, r.y), (r.x, r.y + r.len), r.width)
        r.fall()

    pygame.display.flip()
