#!/usr/bin/python3
# -----------------------------------------------------------------
# Pomotimer using python and pyqt5;
#
#
#
# Author:N84.
#
# Create Date:Tue Nov 22 16:19:10 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from defaults import *
from custom_thread import CustomThread
import sys

# wipe the terminal screen;
Defaults.clear()


class TimerLabel(QLabel):
    """Custom Label for showing the time;"""

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f"""
                            color: {Defaults.LABEL_FG_BASE};
                            font-size: 49px;
                            font-family: {Defaults.WIN_FONT_FAMILY};
                            font-weight: bold;
                           """)

        self.setGeometry(0, 0, 150, 100)

        # setup the timer;
        self.timer = QTimer()
        self.timer.timeout.connect(self.__tick)

        # setup blink timer;
        self.__blink_timer = QTimer()
        self.__blink_timer.timeout.connect(self.__blink)

        self.timer_status = False

    def set_time(self, time: str):
        """
            update the time on the label;

            return None;
        """

        self.setText(time)

        return None

    def get_time(self):
        """
            return the time on the label;

            return str;
        """

        return self.text()

    def wheelEvent(self, event):
        """
            mouse wheel event;
        """

        # guard condition;
        if self.timer_status:
            return None

        # note:
        # -120 => increase "mouse wheel go up"
        # 120 => decrease "mouse wheel go down"
        wheel_event = event.angleDelta().y()

        # value to decrease or increase,
        # depend on the mouse position,
        # if its on minute or seconds;
        if event.x() <= 50:
            value = 60

        elif event.x() >= 70:
            value = 1

        else:
            value = 0

        # now get the time in seconds;
        time_in_seconds = self.__timer_value_to_seconds(self.get_time())

        if wheel_event == -120:
            # increase the timer;

            time_in_seconds -= value

            # guard-condition;
            if time_in_seconds < 0:
                self.set_time("00:00")

                return None

        if wheel_event == 120:
            # decrease the timer;

            time_in_seconds += value

        new_timer_label_value = self.__seconds_to_timer_value(time_in_seconds)

        self.set_time(new_timer_label_value)

        return None

    @ staticmethod
    def __timer_value_to_seconds(timer_value: str):
        """
            convert the time value in this form=> "xx:xx",
            to seconds;

            return int;
        """

        minutes, seconds = timer_value.split(":")

        try:
            return int(minutes) * 60 + int(seconds)

        except ValueError:
            raise Exception("Can't convert minutes or seconds to integers!!!")

    @ staticmethod
    def __seconds_to_timer_value(seconds: int):
        """
            convert the time in seconds into timer label format,
            "xx:xx";

            return string;
        """

        minutes, seconds = divmod(seconds, 60)

        return f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    def __tick(self):
        """
            Start the timer ticking;
            remove one second in every tick;

            return None
        """

        # guard condition;
        if not self.timer_status:
            return None

        time_in_seconds = self.__timer_value_to_seconds(self.get_time())

        time_in_seconds -= 1

        if time_in_seconds < 0:
            # stop the timer if finish;
            self.timer_status = False
            # set the timer to the start point;
            self.set_time("01:00")

            self.__blink_timer.start(500)

            return None

        new_timer_label_value = self.__seconds_to_timer_value(time_in_seconds)

        self.set_time(new_timer_label_value)

        return None

    def __blink(self):
        """"""

        font_color = self.palette().text().color().name()

        if font_color == Defaults.LABEL_FG_BASE:
            self.setStyleSheet(f"""
                            color: {Defaults.LABEL_BLINKING_FG};
                            font-size: 49px;
                            font-family: {Defaults.WIN_FONT_FAMILY};
                            font-weight: bold;
                           """)

        if font_color == Defaults.LABEL_BLINKING_FG:
            self.setStyleSheet(f"""
                            color: {Defaults.LABEL_FG_BASE};
                            font-size: 49px;
                            font-family: {Defaults.WIN_FONT_FAMILY};
                            font-weight: bold;
                           """)

        return None

    def start(self):
        """"""
        self.timer_status = True
        self.timer.start(50)  # time in ms;

        return None

    def stop(self):
        """"""
        self.timer_status = False
        self.timer.stop()

        return None


class MainWindow(QMainWindow):
    """"""

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        self.setFixedSize(Defaults.WIN_WIDTH, Defaults.WIN_HEIGHT)

        self.setWindowTitle(Defaults.TITLE)

        self.setStyleSheet(f"""
                           background-color: {Defaults.BACKGROUND_COLOR};
                           font-family: {Defaults.WIN_FONT_FAMILY};
                           """)

        self.timer_label = TimerLabel(parent=self, text="01:00")

        self.timer_label.move(
            (Defaults.WIN_WIDTH - self.timer_label.width()) // 2 + 11,  # center on x;
            (Defaults.WIN_HEIGHT - self.timer_label.height())//2  # center on y;
        )

        self.timer_label.start()


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
