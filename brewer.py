from controller import Controller

controller = Controller()

def main():
    import code
    code.InteractiveConsole(locals=globals()).interact()

if __name__ == '__main__':
    main()
