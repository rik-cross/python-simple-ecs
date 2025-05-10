# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

class EntityManager:

    '''
    Manages a list of entities and associated entity IDs.
    '''
    
    def __init__(self):

        # set the maximum number of entities allowed
        # (this number is used to create the IDs in the ID pool)
        self._maxEntities = 1000

        # the ID pool is the place that available IDs are taken from
        # and is just a list of numbers from 0 --> _maxEntities
        self.IDPool = [x for x in range(self._maxEntities)]

    def checkoutID(self):

        '''
        Get the next available ID from the pool for assigning to an entity.
        :return int: Returns the first (smallest) number from the ID pool.
        '''
        
        # get the first (lowest) number from the pool
        if len(self.IDPool) > 0:
            return self.IDPool.pop(0)
        
        # return None if no ID is available
        else:
            return None

    def checkinID(self, ID):
        
        '''
        Return an Entity ID back to the pool of available IDs.
        :param int ID: The ID to return to the pool
        '''

        # only return an ID if it's not already in the pool
        if ID not in self.IDPool:

            # add the ID back into the pool
            self.IDPool.append(ID)        
            
            # sort the available IDs, so that they are assigned in low --> high order
            self.IDPool.sort()