# Python Simple ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

import ecs
from TransformComponent import TransformComponent

class PhysicsSystem(ecs.System):

    '''
    The physics system updates the position of all entities
    with a transform component.
    '''
    
    # the physics system only processes entities with transform components
    def init(self):
        self.addRequiredComponentType(TransformComponent)

    # update the position of the entity, and do some very basic collision detection
    def updateEntity(self, scene, entity, deltaTime=1):

        # get the entity transform component
        transformComponent = entity.getComponent(TransformComponent)

        # create new temporary position variables
        newPosX = transformComponent.position[0] + (transformComponent.direction[0] * transformComponent.speed * deltaTime)
        newPosY = transformComponent.position[1] + (transformComponent.direction[1] * transformComponent.speed * deltaTime)

        # create new temporary position variable
        newDirX = transformComponent.direction[0]
        newDirY = transformComponent.direction[1]

        # calculate the radius of the entity
        radius = transformComponent.size / 2

        #
        # screen collision detection
        #

        # left
        if newPosX <= radius:
            newPosX = radius
            newDirX *= -1
        
        # right
        if newPosX >= scene.size[0] - radius:
            newPosX = scene.size[0] - radius
            newDirX *= -1

        # top
        if newPosY <= radius:
            newPosY = radius
            newDirY *= -1
        
        # bottom
        if newPosY >= scene.size[1] - radius:
            newPosY = scene.size[1] - radius
            newDirY *= -1

        # set the new position and direction
        transformComponent.position = [newPosX, newPosY]
        transformComponent.direction = [newDirX, newDirY]