#!/usr/bin/python3
# -----------------------------------------------------------------
# simple pomodoro app using tkinter;
# this is one of my 50 python project challenge;
#
#
# Author:N84.
#
# Create Date:Sat Oct 22 20:24:56 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------
from defaults import Defaults
import time
import tkinter as tk
import threading


Defaults.clear()


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(Defaults.TITLE)

        # set the size of the window;
        self.geometry(f"{Defaults.WIN_WIDTH}x{Defaults.WIN_HEIGHT}")

        # set the background color;
        self.configure(bg=Defaults.BACKGROUND_COLOR)

        # setup the timer var for the label;
        # this variable will update our time on the screen;

        self.timer_value = tk.StringVar()
        # set default value for this var;
        self.timer_value.set("25:00")

        # create the window widgets;
        self.timer_label = tk.Label(
            master=self,
            textvariable=self.timer_value,
            **Defaults.TIMER_LABEL_PROPERTIES
        )

        self.btn = tk.Button(
            master=self,
            command=None,
            image=None,
            text="click",
            **Defaults.BTN_PROPERTIES
        )

        # now place all the widgets after creating them;
        self.place()

    def show(self):
        self.mainloop()

    def place(self):
        """
            place all the widgets on the window;
        """

        # place the label;
        self.timer_label.place(x=140, y=100)

        # place the button;
        self.btn.place(x=185, y=200)

    def __load_images(self):
        """
            load all needed images;

            return dict;
        """
        # import our pictures.
        play_color_pic = tkinter.PhotoImage(
            file="./assests/pictures/play_color.png", name="play_color")

        play_white_pic = tkinter.PhotoImage(
            file="./assests/pictures/play_white.png", name="play_white")

        pause_color_pic = tkinter.PhotoImage(
            file="./assests/pictures/pause_color.png", name="pause_color")

        pause_white_pic = tkinter.PhotoImage(
            file="./assests/pictures/pause_white.png", name="pause_white")

        return {
            "play_color": play_color_pic,
            "play_white": play_white_pic,
            "pause_color": pause_color_pic,
            "pause_white": pause_white_pic
        }


def main():
    app = App()
    app.show()


if __name__ == "__main__":
    main()
