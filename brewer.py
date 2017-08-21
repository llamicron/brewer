from brewer.controller import Controller
from brewer.slack import BrewerBot
from brewer.recipe import Recipe
import brewer.procedures

import code

controller = Controller()
bot = BrewerBot()


def main():
    code.InteractiveConsole(locals=globals()).interact()


if __name__ == '__main__':
    main()
