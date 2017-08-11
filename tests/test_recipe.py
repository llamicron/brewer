import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from recipe import Recipe
import unittest

class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()

