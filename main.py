# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public Licence version 2 as published by the Free Software Foundation.

from lib import *
from evdev import ecodes
from actions import on_press
from threading import Thread
listener = Listener()


mod_keys = {
    ecodes.KEY_LEFTSHIFT: 'shift',
    ecodes.KEY_RIGHTSHIFT: 'shift',
    ecodes.KEY_LEFTCTRL: 'ctrl',
    ecodes.KEY_RIGHTCTRL: 'ctrl',
    ecodes.KEY_LEFTALT: 'alt',
    ecodes.KEY_RIGHTALT: 'alt',
    ecodes.KEY_LEFTMETA: 'meta',
    ecodes.KEY_RIGHTMETA: 'meta'
}
transformer = {
    'shift': 'S',
    'ctrl': 'C',
    'alt': 'A',
    'meta': 'M'
}


class Main:
    def __init__(self):
        while True:
            action = listener.get_event()
            if not action:
                continue
            if action.type == 1 or action.type == 2:
                if action.key not in mod_keys.keys():
                    keystroke = get_keystroke(action.device, action.key)
                    Thread(target=on_press, args=(keystroke,)).start()


def get_current_mods(device: int):
    mods = {
        'ctrl': False,
        'meta': False,
        'alt': False,
        'shift': False
    }
    pressed_mod_keys = [key for key in listener.get_pressed_keys(device) if key in mod_keys.keys()]
    for key in pressed_mod_keys:
        mods[mod_keys[key]] = True
    return mods

def get_current_mods_as_list(device: int):
    return [mod for mod, value in get_current_mods(device).items() if value == True]

def get_keystroke(device: int, key: int):
    keys = [transformer[key] for key in get_current_mods_as_list(device)]
    keys.append(ecodes.KEY[key][4:].lower())
    return '-'.join(keys)
    

if __name__ == '__main__':
    Main()
