# Python Simple ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import pygame
import ecs
from TransformComponent import TransformComponent
from SpriteComponent import SpriteComponent

class GraphicsSystem(ecs.System):

    '''
    The graphics system is responsible for drawing entities that
    have a sprite component. It also draws some text to the screen.
    '''

    def init(self):

        # the transform and sprite components are required
        self.addRequiredComponentType(TransformComponent)
        self.addRequiredComponentType(SpriteComponent)
        
        # create a font and text surface to display
        self.font = pygame.font.SysFont('arial', 18)
        self.textSurface = self.font.render('Pygame ECS example', False, (0, 0, 0))

    def draw(self, scene, surface = None):
        
        # draw the text surface to the screen once per frame
        surface.blit(self.textSurface, (0, 0))
        
    def drawEntity(self, scene, entity, surface = None):
        
        # get the entity's required components
        transformComponent = entity.getComponent(TransformComponent)
        spriteComponent = entity.getComponent(SpriteComponent)

        # draw the entity as a circle, using the position, size and color data
        pygame.draw.circle(surface, spriteComponent.color, transformComponent.position, transformComponent.size // 2)