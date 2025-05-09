# Python Simple ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import pygame
import random
import ecs

from TransformComponent import TransformComponent
from SpriteComponent import SpriteComponent
from PhysicsSystem import PhysicsSystem
from GraphicsSystem import GraphicsSystem

# initialise Pygame
pygame.init()

# setup screen to required size
screen = pygame.display.set_mode((680, 460))
pygame.display.set_caption('Pygame ECS Example 2')
clock = pygame.time.Clock() 

# create a scene, and add a size
scene = ecs.Scene()
scene.size = (680, 460)

# create 500 entities with position and sprite components
# containing random values, and add to the scene
for _ in range(500):
    scene.addEntity(
        ecs.Entity(
            TransformComponent(
                position = (random.randint(10, 670), random.randint(10, 450)),
                direction = (random.random() * 2 - 1, random.random() * 2 - 1),
                size = random.randint(10, 30),
                speed = random.randint(2,4)
            ),
            SpriteComponent(random.choice([
                    (224, 187, 228),
                    (149, 125, 173),
                    (210, 145, 188),
                    (254, 200, 216),
                    (255, 223, 211)
            ]))
        )
    )

# create a physics system instance and add to the scene
scene.addSystem(PhysicsSystem())
scene.addSystem(GraphicsSystem())

# game loop
running = True
while running:

    # advance clock at 60 FPS
    clock.tick(60)

    # respond to quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #
    # update
    #

    scene.update()

    #
    # draw
    #
  
    # clear screen to Cornflower Blue
    screen.fill('cornflowerblue')

    scene.draw(screen)

    # draw to the screen
    pygame.display.flip()

# quit Pygame on exit
pygame.quit()