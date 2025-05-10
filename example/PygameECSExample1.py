# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import pygame
import specs

from TransformComponent import TransformComponent
from SpriteComponent import SpriteComponent
from PhysicsSystem import PhysicsSystem
from GraphicsSystem import GraphicsSystem

# initialise Pygame
pygame.init()

# setup screen to required size
screen = pygame.display.set_mode((680, 460))
pygame.display.set_caption('Pygame ECS Example 1')
clock = pygame.time.Clock() 

# create a scene
scene = specs.Scene()
scene.size = (680, 460)

# create an entity with a position component
# and add to the scene
entity = specs.Entity()
entity.addComponent(TransformComponent(
    position = (50, 50),
    direction = (1, 1),
    size = 100,
    speed = 2)
)
entity.addComponent(SpriteComponent((224, 187, 228)))
scene.addEntity(entity)

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