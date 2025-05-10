# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

class Scene:

    '''
    A scene is a collection of entities and systems.
    Systems added to the scene will process all appropriate entities added to the scene.
    '''

    # a static list of all scenes
    scenes = []

    def __init__(self):

        # add this scene to the static list of all scenes
        Scene.scenes.append(self)

        # initially the scene is empty
        self.entities = []
        self.systems = []
    
    #
    # entities
    #

    def addEntity(self, entity):

        '''
        Adds the specified entity to the scene.
        :param ecs.Entity entity: The entity to add.
        '''

        # an entity should only appear in a scene once
        if entity not in self.entities:

            # add the entity to the scene
            self.entities.append(entity)

            # call the scene's onAddedToScene() method
            # for the added entity
            self.onEntityAddedToScene(entity)
        
    def removeEntity(self, entity):

        '''
        Removes the specified entity from the scene.
        :param ecs.Entity entity: The entity to remove. 
        '''
        
        # only attempt to remove entities that exist in the scene
        if entity in self.entities:
        
            # remove the entity
            self.entities.remove(entity)
        
            # call the scene's onRemovedFromScene() method
            # for the removed entity
            self.onEntityRemovedFromScene(entity)
    
    #
    # systems
    #

    def addSystem(self, system):

        '''
        Adds the specified system to the scene.
        :param ecs.System system: The system to add.
        '''
        
        # only add a system type once
        for s in self.systems:
            if type(system) is type(s):
                return

        # add the system
        self.systems.append(system)

    def removeSystem(self, system):

        '''
        Removes the specified system from the scene.
        :param ecs.System system: The system to remove.
        '''

        # remove the system if it exists in the scene
        if system not in self.systems:
            self.systems.remove(system)

    #
    # scene game loop methods
    #

    def update(self, deltaTime = 1):

        '''
        Update method is called once per frame, and runs the
        update() and updateEntity() method for all systems.
        This method also deletes entities marked for deletion.
        :param float deltaTime: The elapsed time (default = 1).
        '''

        # run each system in the scene
        for system in self.systems:

            # call the main system update() method once per frame
            system.update(self, deltaTime=1)
            
            # call the scene updateEntity() method once per frame
            # on each entity that has all of the required component types
            for entity in self.entities:

                # check if the entity has all required components
                entityHasAllRequiredComponents = True
                for requiredComponentType in system.requiredComponentTypeList:
                    if entity.getComponent(requiredComponentType) is None:
                        entityHasAllRequiredComponents = False
                        break
                
                # process all active entities with the required components
                if entityHasAllRequiredComponents is True and entity.active is True:
                    system.updateEntity(self, entity, deltaTime = 1)

            #
            # clean-up
            #

            # delete all entities in the scene that are marked for deletion
            # looping backwards through the list to avoid skipping entities
            for i in range(len(self.entities) - 1, -1, -1):
                if self.entities[i]._markedForDeletion == True:
                    entityToDelete = self.entities[i]
                    # remove all components
                    entityToDelete.removeAllComponents()
                    # delete the entity from all scenes
                    for scene in Scene.scenes:
                        scene.entities.remove(entityToDelete)
                    # TODO - is this needed?
                    del entityToDelete
                    
    def draw(self, surface = None):

        '''
        Draw method is called once per frame, and runs the
        draw() and drawEntity() for all systems.
        :param any surface: The (optional) surface to draw to.
        This can be any type of surface, depending on what is used in the systems (default = None).
        '''
        
        # run each system in the scene
        for system in self.systems:

            # call the main system draw() method once per frame
            # for those systems drawing below entities
            if system.drawAfterEntities is False:
                system.draw(self, surface)
            
            # call the scene drawEntity() method once per frame
            # on each entity that has all of the required component types
            for entity in self.entities:
                entityHasAllRequiredComponents = True

                # check if the entity has all required components
                for requiredComponentType in system.requiredComponentTypeList:
                    if entity.getComponent(requiredComponentType) is None:
                        entityHasAllRequiredComponents = False
                        break
                
                # process all active entities with the required components
                if entityHasAllRequiredComponents is True and entity.active is True:
                    system.drawEntity(self, entity, surface)

            # call the main system draw() method once per frame
            # for those systems drawing above entities
            if system.drawAfterEntities is True:
                system.draw(self, surface)

    #
    # user-defined methods to override
    #

    def onEntityAddedToScene(self, entity):

        '''
        Method is run when an entity is added to the scene.
        :param ecs.Entity entity: The entity added.
        '''
        
        pass

    def onEntityRemovedFromScene(self, entity):
        
        '''
        Method is run when an entity is removed from the scene.
        :param ecs.Entity entity: The entity removed.
        '''
        
        pass