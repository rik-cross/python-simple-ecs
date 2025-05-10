# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

class Component:
    
    '''
    Base component class.
    Components can derive from this class, but don't have to.
    '''

    def onAddedToEntity(self, entity):

        '''
        Callback that is run when a component is added to an entity.
        :param ecs.Entity entity: The entity to which the component has been added.
        '''
        
        pass

    def onRemovedFromEntity(self, entity):

        '''
        Callback that is run when a component is removed an entity.
        This includes instances when an entity is deleted.
        :param ecs.Entity entity: The entity for which the component has been removed.
        '''
        
        pass

    def reset(self, entity):
        
        '''
        Callback that is run when a component is reset.
        :param ecs.Entity entity: The entity for which the component has been removed.
        '''
        
        pass
