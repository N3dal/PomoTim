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
import _thread
from sys import exit


# TODO: add reset button that appears only when we stop the timer;


Defaults.clear()


class CustomThread:
    """
        custom thread class with stop method;
    """

    def __init__(self, func, name: str, args=tuple()):

        self.func = func
        self.args = args
        self.name = name
        self.thread_id = None

        self.__stop_flag = True

        # set the stop and start flag;
        # self.__stop_flag = threading.Event()

    def stop(self):
        """Exit from the thread;"""

        _thread.exit()

        return None

    def run(self):

        self.thread_id = _thread.start_new_thread(self.func, self.args)

        return None

    def get_id(self):
        """
            return the thread identifier;

        """

        return self.thread_id


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(Defaults.TITLE)

        # set the size of the window;
        self.geometry(f"{Defaults.WIN_WIDTH}x{Defaults.WIN_HEIGHT}")

        # set the background color;
        self.configure(bg=Defaults.BACKGROUND_COLOR)

        # make the window un-resizable;
        self.resizable(0, 0)

        # load all the images;
        self.images = self.__load_images()

        # setup the timer var for the label;
        # this variable will update our time on the screen;

        self.timer_value = tk.StringVar()
        # set default value for this var;
        self.timer_value.set("15:00")

        # create the window widgets;
        self.timer_label = tk.Label(
            master=self,
            textvariable=self.timer_value,
            **Defaults.TIMER_LABEL_PROPERTIES
        )

        self.btn = tk.Button(
            master=self,
            command=self.__btn_event,
            image=self.images["play_white"],
            text="click",
            ** Defaults.BTN_PROPERTIES
        )

        # now place all the widgets after creating them;
        self.place()

        # setup the timer status,
        # that we will use it for stop and staring the timer;
        # False for stop the timer and True for start the timer;
        self.__timer_status = False

        # set the tick-thread;

        self.__tick_thread = CustomThread(
            func=self.__timer_tick, name="tick_thread"
        )

        self.__blinking_thread = CustomThread(
            func=self.__label_blinking, name="label_blinking"
        )

        self.start_app()

    def place(self):
        """
            place all the widgets on the window;
        """

        # place the label;
        self.timer_label.place(x=150, y=100)

        # place the button;
        self.btn.place(x=185, y=180)

    def start_app(self, **options):
        """
            start the app;
        """

        self.mainloop()

    def __load_images(self):
        """
            load all needed images;

            return dict;
        """
        # import our pictures.
        play_color_pic = tk.PhotoImage(
            file="./assests/pictures/play_color.png", name="play_color")

        play_white_pic = tk.PhotoImage(
            file="./assests/pictures/play_white.png", name="play_white")

        pause_color_pic = tk.PhotoImage(
            file="./assests/pictures/pause_color.png", name="pause_color")

        pause_white_pic = tk.PhotoImage(
            file="./assests/pictures/pause_white.png", name="pause_white")

        return {
            "play_color": play_color_pic,
            "play_white": play_white_pic,
            "pause_color": pause_color_pic,
            "pause_white": pause_white_pic
        }

    def __timer_tick(self):
        """
            start the timer or stop it;
        """

        # get the time from the timer label, the minutes and seconds;
        timer_label_value_minutes, timer_label_value_seconds = self.timer_value.get().split(":")

        # and turn it to seconds;
        timer_value_in_seconds = int(
            timer_label_value_minutes) * 60 + int(timer_label_value_seconds)

        while timer_value_in_seconds > -1 and self.__timer_status:
            time_in_minutes, time_in_seconds = divmod(
                timer_value_in_seconds, 60)
            timer_value_in_seconds -= 1

            timer_new_value = f"{str(time_in_minutes).zfill(2)}:{str(time_in_seconds).zfill(2)}"

            # now update the timer value;
            self.timer_value.set(timer_new_value)
            time.sleep(1)

        return None

    def __btn_event(self):
        """
            start/pause button event;

            return None
        """

        if self.btn.cget("image") == "play_white":

            self.btn.configure(image=self.images["pause_white"])
            self.__timer_status = True

            try:
                # self.__tick_thread.start()
                self.__tick_thread.run()

            except RuntimeError:
                # if we click on the button multiple times;
                print("Timer Tick Threading!")
                return None

        elif self.btn.cget("image") == "pause_white":

            self.btn.configure(image=self.images["play_white"])
            self.__timer_status = False

            try:
                self.__blinking_thread.run()

            except RuntimeError:
                print("blinking Threading!")
                return None

        return None

    def __label_blinking(self):
        """
            simple event that will cause to change the color of the,
            label to blue then to the white if we stop the timer,
            and keep blinking until we start the timer again;

            return None;
        """

        while not self.__timer_status:

            self.timer_label.configure(fg=Defaults.LABEL_BLINKING_FG)
            self.update()
            time.sleep(0.5)  # sleep for half millisecond;

            self.timer_label.configure(fg=Defaults.LABEL_FG_BASE)
            self.update()
            time.sleep(0.5)  # sleep for half millisecond;

        return None


def main():
    app = App()


if __name__ == "__main__":
    main()
