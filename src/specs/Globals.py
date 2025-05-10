# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

# import the manager class definitions
from .EntityManager import EntityManager
from .ComponentManager import ComponentManager

# create global manager instances
_entityManager = EntityManager()
_componentManager = ComponentManager()