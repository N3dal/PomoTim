"""
    contain all the defaults needed for this program to work fine;
"""

from os import name as OS_NAME
from os import system


class Defaults:
    """"""
    TITLE = "PomoTim"

    # notice that those also are the minimum width and height;
    WIN_WIDTH = 250
    WIN_HEIGHT = 250
    BACKGROUND_COLOR = "#fafafa"
    WIN_FONT_FAMILY = "Ubuntu"
    LABEL_FG_BASE = "#484b6a"
    LABEL_BLINKING_FG = "#cd1b5b"

    @staticmethod
    def clear():
        """
            wipe terminal screen;
        """

        if OS_NAME == "posix":
            # for *nix machines;
            system("clear")

        elif OS_NAME == "windows":
            system("cls")

        else:
            # for all other os in this world;
            # system("your-command")
            pass

        return None
