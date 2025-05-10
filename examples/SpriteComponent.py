# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import specs

class SpriteComponent(specs.Component):

    def __init__(self, color):
        self.color = color