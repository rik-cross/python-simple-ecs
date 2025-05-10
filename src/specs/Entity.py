# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

from .Globals import _entityManager, _componentManager

class Entity:

    '''
    An entity is really just an ID used to group a collection of components.
    :param ecs.Component component: An optional component to add to the entity.
    :param list(ecs.Component) moreComponents: Additional optional components to add to the entity.
    '''

    def __init__(self, component = None, *moreComponents):

        # get an available ID from the entity manager
        # and assign it to the entity (if an ID is available)
        ID = _entityManager.checkoutID()
        if ID is None:
            raise Exception('No Entity ID available, maximum number of entities created.')
        self.ID = ID

        # add any specified components to the entity
        for c in [component] + list(moreComponents):
            self.addComponent(c)

        # systems only process active entities
        self.active = True

        # a scene deletes entities with _markedForDeletion = True
        # at the end of each game loop, which avoids 
        self._markedForDeletion = False
        self.tags = []

        # add the entity to the entity manager's list of all entities
        #entityManager.entities.append(self)

    #
    # core
    #

    def destroy(self):

        '''
        Marks the entity for deletion,
        which will happen after each system has finished processing entities.
        '''
        
        self._markedForDeletion = True

    #
    # tags
    #

    def addTag(self, tag, *moreTags):
        
        '''
        Add one or more tags to an entity, with no duplicates allowed.
        :param str tag: The tag to add to the entity.
        :param list(str) moreTags: Additional optional tags to add to the entity.
        '''
        
        # add each tag specified
        for t in [tag] + list(moreTags):
            # only add a tag is not already present
        
            if self.hasTag(t) is False:
                self.tags.append(t)

    def hasTag(self, tag, *moreTags):
        
        '''
        Checks whether an entity includes one or more tags.
        :param str tag: The tag to check.
        :param list(str) moreTags: Additional optional tags to check.
        :return bool: Returns True if the entity has all tags.
        '''
        
        # create a list of all tags to check
        tags = [tag] + list(moreTags)
        
        # tags are all contained in self.tags if it is a subset
        return set(tags).issubset(self.tags)

    def removeTag(self, tag, *moreTags):
        
        '''
        Removes one or more tags from an entity, if they exist.
        :param str tag: The tag to remove from the entity.
        :param list(str) moreTags: Additional optional tags to remove from the entity.
        '''
        
        # remove all tags if they exist
        for t in [tag] + list(moreTags):
            if t in self.tags:
                self.tags.remove(t)

    #
    # components
    #

    def addComponent(self, component):

        '''
        Adds a component to the entity.
        :param ecs.Component component: The component to add.
        '''
        
        # a component will need to be registered the first time a component
        # of a particular type is added to an entity
        if _componentManager.isComponentTypeRegistered(type(component)) is False:
            _componentManager.registerComponentType(type(component))
        
        # add the component using the component manager
        _componentManager.addComponentToEntity(self, component)

    def hasComponent(self, componentType):

        '''
        :param type(ecs.Component) componentType: The type of the component to check.
        :return bool: Returns True if the entity has a component of the specified type.
        '''
        
        # check if the component exists for the entity via the component manager
        return _componentManager.hasComponent(self, componentType)

    def getComponent(self, componentType):

        '''
        Gets the component of the specified type.
        :param type(ecs.Component): The type of the component to get.
        :return ecs.Component: Returns the component of the specified type, or None if no component exists.
        '''
        
        # get the component stored in the component manager 2D array
        return _componentManager.getComponentForEntity(self, componentType)

    def resetAllComponents(self):

        '''
        Runs the reset() method for all components.
        '''
        
        # defer to the component manager to reset all components for the entity
        _componentManager.resetAllComponentsForEntity(self)

    def removeComponent(self, componentType):

        '''
        Remove the component of the specified type.
        :param type(ecs.Component) componentType: The type of the component to remove.
        '''
        
        # defer to the component manager to remove and return the component
        _componentManager.removeComponentTypeFromEntity(self, componentType)

    def removeAllComponents(self):

        '''
        Removes all components.
        '''
        
        # defer to the component manager to remove all components
        _componentManager.removeAllComponentsForEntity(self)