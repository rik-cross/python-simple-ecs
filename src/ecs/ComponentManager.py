# Python Simple ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

class ComponentManager:
    
    '''
    The ComponentManager assigns component types an ID, and stores
    components for all entities in a [componentID][entityID] 2D array.
    '''

    def __init__(self):

        # TODO - how to avoid this circular dependency?
        from .Globals import _entityManager

        # the maximum different component types that can be registered
        # this is required to determine the Entity/Component array size
        self._maxComponentTypes = 100

        # a list of registered component types
        # the ID of a component type is its position in the list
        self._registeredComponentTypes = []

        # a 2D array storing components for all entities
        # access a component for an entity via _entityComponentMap[componentID][entityID]
        self._entityComponentMap = [[None for _ in range(_entityManager._maxEntities)] for _ in range(self._maxComponentTypes)]

    def registerComponentType(self, componentType):

        '''
        Registers a component type (component types cannot be unregistered).
        :param type(ecs.Component) componentType: The type of the component to register.
        :return int: Returns the ID of the registered component.
        '''
        
        # register the component if not yet registered
        if self.isComponentTypeRegistered(componentType) is False:
            self._registeredComponentTypes.append(componentType)
            
        # return the ID of the component type
        return self._registeredComponentTypes.index(componentType)
    
    def isComponentTypeRegistered(self, componentType):

        '''
        Returns whether the specified component type has been registered
        :param type(ecs.Component) componentType: The type of component to check.
        :return bool: Returns True if the component type is registered.
        '''
        
        return componentType in self._registeredComponentTypes

    def hasComponent(self, entity, componentType):
        
        '''
        Returns True if a component of the specified type exists for an entity.
        :param ecs.Entity entity: The entity to check.
        :param type(ecs.Component) componentType: The type of component to check.
        :return bool: Returns True if a component of the specified type exists for an entity.
        '''
        
        # the component type must be registered and
        # a component of that type should exist for the specified entity
        return self.isComponentTypeRegistered(componentType) and \
        self._entityComponentMap[self.getComponentTypeID(componentType)][entity.ID] is not None

    def getComponentForEntity(self, entity, componentType):

        '''
        Fetches a component of a particular type for an entity.
        :param type(ecs.Component) componentType: The type of component to fetch.
        :return ecs.Component: Returns the component of the type specified for an entity (or None if one doesn't exist). 
        '''
        
        # return None for unregistered components
        if componentType not in self._registeredComponentTypes:
            return None
        
        # get the IDs for the entity and the component
        entityID = entity.ID
        componentID = self.getComponentTypeID(componentType)
        
        # use the IDs to access the component for the entity
        # in the entityComponentMap 2D array
        return self._entityComponentMap[componentID][entityID]

    def getComponentTypeID(self, componentType):

        '''
        Gets the ID for a specified component type.
        :param type(ecs.Component) componentType: The type of component to get the ID for.
        :return int: Returns the ID of the registered type, or None if type not registered.
        '''
        
        # return None if the component type is not registered
        if self.isComponentTypeRegistered(componentType) is False:
            return None
        
        # return the ID, which is the position of the component type
        # in the known component types list
        return self._registeredComponentTypes.index(componentType)

    def addComponentToEntity(self, entity, component):

        '''
        Associated a component with an entity.
        :param ecs.Entity entity: The entity to link the component to.
        :param ecs.Component component: The component to add to the entity. 
        '''

        # get the IDs of the entity and the component
        entityID = entity.ID
        componentID = self.getComponentTypeID(type(component))
        
        # only add known component types to entities
        if componentID is not None:

            # add the component into the entityComponentMap 2D array
            # the position of the component is [componentID][entityID]
            self._entityComponentMap[componentID][entityID] = component

            # run the component's onAddedToEntity callback if one exists
            if hasattr(component, 'onAddedToEntity'):
                component.onAddedToEntity(entity)
        
        # raise an exception if trying to add unregistered component types
        else:
            raise Exception('Cannot add', type(component), '- type not registered.')
    
    def removeComponentTypeFromEntity(self, entity, componentType):

        '''
        Removes a component of the specified type from the specified entity.
        :param ecs.Entity entity: The entity to remove the component from.
        :param type(ecs.Component) componentType: The type of component to remove.
        '''
        
        # get the IDs for the entity and the component
        entityID = entity.ID
        componentID = self.getComponentTypeID(componentType)
        
        # get the component for the specified entity
        component = self.getComponentForEntity(entity, componentType)

        if component is not None:

            # run the component's onRemovedFromEntity callback if one exists
            if hasattr(component, 'onRemovedFromEntity'):
                component.onRemovedFromEntity(entity)
        
            # remove the component from the entityComponentMap array
            self._entityComponentMap[componentID][entityID] = None

        return component

    def resetAllComponentsForEntity(self, entity):

        '''
        Calls the reset() method on all components for an entity.
        :param ecs.Entity entity: The entity to reset.
        '''

        # try to reset components of all registered types
        for componentType in self._registeredComponentTypes:
            
            # get the component of the specified type
            component = self.getComponentForEntity(entity, componentType)

            # call reset method, if one exists
            if component is not None and hasattr(component, 'reset'):
                component.reset(entity)

    def removeAllComponentsForEntity(self, entity):

        '''
        Removes all components for an entity.
        :param ecs.Entity entity: The entity to remove all entities for.
        '''

        # call existing remove component type method
        # for all registered component types
        for componentType in self._registeredComponentTypes:
            self.removeComponentTypeFromEntity(entity, componentType)