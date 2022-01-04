# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public Licence version 2 as published by the Free Software Foundation.

import evdev
from select import select
from evdev import ecodes
from atexit import register


device_names = ["Dell Dell USB Entry Keyboard"]


class Listener:
    def __init__(self):
        self.devices = []
        register(self.__exit)
        for device in [evdev.InputDevice(path) for path in evdev.list_devices()]:
            if device.name in device_names:
                self.devices.append(device)
        for device in self.devices:
            device.grab()
        self.device_fds = {device.fd: device for device in self.devices}

    def get_event(self, timeout=None):
        r, w, x = select(self.device_fds, [], [], timeout)
        for fd in r:
            for event in self.device_fds[fd].read():
                if event.type == evdev.ecodes.EV_KEY:
                    return Action(event, self.device_fds[fd])
        return None
    
    def __exit(self):
        for device in self.devices:
            device.close()
    
    def get_pressed_keys(self, device: int):
        return [key for key in self.devices[device].active_keys()]
        

class Action:
    def __init__(self, event, device):
        self.key = event.code
        self.type = event.value
        self.device = device_names.index(device.name)


def int_to_name(key: int):
    return ecodes.KEY[key]
