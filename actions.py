# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public Licence version 2 as published by the Free Software Foundation.

from threading import Thread
from os import system, chdir
import subprocess



tmux_actions = {
    "left": "select-pane -L",
    "right": "select-pane -R",
    "up": "select-pane -U",
    "down": "select-pane -D",
    "w": "split-window -b",
    "a": "split-window -hb",
    "s": "split-window",
    "d": "split-window -h",
    "f": "resize-pane -L",
    "h": "resize-pane -R",
    "g": "resize-pane -D",
    "t": "resize-pane -U",
    "l": "send clear && tmux send enter",
    "esc": "kill-pane",
    "C-tab": "select-window -t:+1",
    "C-S-tab": "select-window -t:-1",
    "C-t": "neww"
}

chdir("/home/max/")


# This function is called when the user presses a key on the secondary keyboard.
# Keystroke is the list of keys pressed in the form "Mod-Mod-Mod-Key", Mod being a letter for a modifier (e.g. "C" for Control)
def on_press(keystroke, device):
    if get_window_title().endswith(": tmux: client — Konsole"):
        try:
            system("tmux " + tmux_actions[keystroke])
        except KeyError:
            pass

def get_window_title():
    return subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"]).decode("utf-8").split("\n")[0]
