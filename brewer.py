from controller import Controller
from slack import BrewerBot
from recipe import Recipe
import procedures
import code

controller = Controller()
bot = BrewerBot()

def main():
    code.InteractiveConsole(locals=globals()).interact()

if __name__ == '__main__':
    main()
