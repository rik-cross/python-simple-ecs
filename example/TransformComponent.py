# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import specs

class TransformComponent(specs.Component):

    def __init__(self, position, direction, size, speed):
        self.position = position
        self.direction = direction
        self.size = size
        self.speed = speed

