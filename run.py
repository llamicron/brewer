from brewer.controller import Controller
from brewer.slack import BrewerBot
from brewer.version import VERSION

import code

controller = Controller()
bot = BrewerBot()


def main():
    print(("Brewer version %s" % VERSION))
    code.InteractiveConsole(locals=globals()).interact()


if __name__ == '__main__':
    main()
