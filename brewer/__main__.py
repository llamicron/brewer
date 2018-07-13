#!/usr/bin/env python
from IPython import embed
from brewer.controller import Controller
from brewer.version import VERSION

controller = Controller()
bot = BrewerBot()

print("Brewer version %s" % VERSION)

embed()
