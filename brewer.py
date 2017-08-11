from controller import Controller
from slack import BrewerBot
from recipe import Recipe
import code

controller = Controller()
bot = BrewerBot()
recipe = Recipe({
    "name": "Mexican Lager",
    "grain_temp": 80,
    "mash_temp": 150,
    "mash_time": 3600,
})

def main():
    code.InteractiveConsole(locals=globals()).interact()

if __name__ == '__main__':
    main()
