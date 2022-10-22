"""
    contain all the defaults needed for this program to work fine;
"""

from os import name as OS_NAME
from os import system


class Defaults:
    """"""
    TITLE = "PomoTim"
    WIN_WIDTH = 400
    WIN_HEIGHT = 300
    BACKGROUND_COLOR = "gray25"
    WIN_FONT_FAMILY = "Ubuntu"

    TIMER_LABEL_PROPERTIES = {

        "bg": BACKGROUND_COLOR,
        "font": (WIN_FONT_FAMILY, 28, "bold"),
        "highlightthickness": 1,
        "highlightbackground": "gray21",
        "fg": "gray85"

    }

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
