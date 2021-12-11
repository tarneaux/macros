from evdev.ecodes import *
import subprocess


def from_en_us_to_fr_fr(key_code):
    """
    Convert a linux key code from en_US to fr_FR.
    Example:
    >>> from_en_us_to_fr_fr(KEY_A)
    KEY_Q
    """
    # Get US layout file
    us_layout_file = subprocess.check_output(["gzip", "-dc", "/usr/share/kbd/keymaps/i386/qwerty/us.map.gz"])
    # Get FR layout file
    fr_layout_file = subprocess.check_output(["gzip", "-dc", "/usr/share/kbd/keymaps/i386/azerty/fr.map.gz"])
    # 

if __name__ == "__main__":
    from_en_us_to_fr_fr(KEY_A)
