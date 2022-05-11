# macros

Disclaimer: this is a personal program. I have published it to help anyone wanting to do the same kind of thing and I am not responsible for any damage that may occur to your computer.


This program allows you to create macros for a secondary keyboard on Linux. It uses the python evdev library to block and read the secondary keyboard.

## Dependencies

You only need to install the python evdev library.


## Usage

This program has only been tested on Linux, and will not work on Windows or Mac, because evdev is not available on those platforms.

In `lib.py`, the list device_names is the list of devices which should be grabbed and listened to. You can find the device names by running `evtest` (after installation) in a terminal.

Now that you have the device names, set the actions you want in `actions.py`. It already contains a few examples. When a key is pressed, the function `on_press` is called. The `keystroke` argument is a string defined by:
- The modifier keys (shift, ctrl, alt and meta) in their one-letter form (e.g. `S` for shift)
- The key itself as outputted by the evdev lib (e.g. `a` for a and `up` for up arrow)

You can find the key names in the [linux kernel source](https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h) or by running `evtest` in a terminal. The KEY_ start of the name is removed and the remaining string is converted to lowercase to prevent errors with the modifier key abbreviations.
