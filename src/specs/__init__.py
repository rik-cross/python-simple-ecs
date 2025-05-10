# Simple Python ECS
#  -- By Rik Cross
#  -- MIT licenced, free to use, modify and distribute

__version__ = "0.1.0"
__author__ = 'Rik Cross'
__license__ = 'MIT'

from .Entity import Entity
from .Component import Component
from .System import System

from .EntityManager import EntityManager
from .ComponentManager import ComponentManager

from .Scene import Scene

from .Globals import *
