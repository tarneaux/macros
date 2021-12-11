

from lib import *
listener = Listener()


class Main:
    def __init__(self):
        while True:
            action = listener.get_event()
            if not action:
                continue
            if action.type == 1:
                print(action.key)


if __name__ == '__main__':
    Main()
