import unittest
import os
import sys
from ..brewer.slack import BrewerBot

class SlackTestCase(unittest.TestCase):
    def setUp(self):
        self.bot = BrewerBot()
        self.bot.channel = "@luke"

    def test_get_token_from_file(self):
        assert isinstance(self.bot.get_token_from_file(), str)

    def test_send_message(self):
        assert self.bot.send(" :beer: Test's are running")
