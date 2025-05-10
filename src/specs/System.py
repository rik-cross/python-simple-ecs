# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

class System:

    def __init__(self):

        '''
        A system processes entities containing specific sets of components.
        '''

        # set the system draw order
        self.drawAfterEntities = True

        # initially there are no requirements, which means the
        # system would process all entities in a scene
        self.requiredComponentTypeList = []

        # run the user-defined init() method
        self.init()

    #
    # setting system requirements
    #

    def addRequiredComponentType(self, componentType, *otherComponentTypes):
        
        '''
        Add one or more component type requirements to a system.
        Systems only run on the entities that have all of the required components.
        :param type(ecs.Component) componentType: The component type to add as a requirement.
        :param list(type(ecs.Component)) otherComponentTypes: Additional optional component types to add.
        '''

        # add each component type to the required list (if not already added)
        for componentType in [componentType] + list(otherComponentTypes):
            if componentType not in self.requiredComponentTypeList:
                self.requiredComponentTypeList.append(componentType)

    def removeRequiredComponentType(self, componentType, *otherComponentTypes):
        
        '''
        Removes one or more component type requirements from a system.
        Systems only run on the entities that have all of the required components.
        :param type(ecs.Component) componentType: The component type to remove as a requirement.
        :param list(type(ecs.Component)) otherComponentTypes: Additional optional component types to remove.
        '''

        # remove each component type from the required list (if present)
        for componentType in [componentType] + list(otherComponentTypes):
            if componentType in self.requiredComponentTypeList:
                self.requiredComponentTypeList.remove(componentType)

    #
    # system update and draw methods
    #

    def init(self):

        '''
        This method is called once when a system is initialised.
        '''
        
        pass

    def update(self, scene, deltaTime = 1):
        
        '''
        This method is called once per frame. It is an overall,
        scene-level method, so doesn't act on individual entities directly.
        :param ecs.Scene scene: The scene running the method.
        :param float deltaTime: The elapsed game time (default = 1).
        '''
        
        pass

    def draw(self, scene, surface = None):
        
        '''
        This method is called once per frame. It is an overall,
        scene-level method, so doesn't act on individual entities directly.
        :param ecs.Scene scene: The scene running the method.
        :param any surface: The surface to draw to.
        The type depends on what is being used in the systems (default = None).
        '''       
        
        pass

    def updateEntity(self, scene, entity, deltaTime = 1):
        
        '''
        This method is called once per frame, for each entity in the scene.
        It is an entity-level method that acts on a specific entity.
        :param ecs.Scene scene: The scene running the method.
        :param ecs.Entity entity: The entity to process.
        :param float deltaTime: The elapsed game time (default = 1).
        '''
        
        pass

    def drawEntity(self, scene, entity, surface = None):
        
        '''
        This method is called once per frame, for each entity in the scene.
        It is an entity-level method that acts on a specific entity.
        :param ecs.Scene scene: The scene running the method.
        :param ecs.Entity entity: The entity to process.
        :param any surface: The surface to draw to.
        The type depends on what is being used in the systems (default = None).
        '''
        
        pass