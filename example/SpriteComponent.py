# Python Simple ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import ecs

class SpriteComponent(ecs.Component):

    def __init__(self, color):
        self.color = color