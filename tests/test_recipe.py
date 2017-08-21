import os
import sys
from ..brewer.recipe import Recipe
import unittest

class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()

