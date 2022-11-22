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

    def set_time(self, time: str):
        """
            update the time on the label;

            return None;
        """

        return None

    def get_time(self):
        """
            return the time on the label;

            return str;
        """

        return self.text()

    def __format_time(self):
        pass

    def __timer_value_to_seconds(self):
        """
            convert the time value in this form=> "xx:xx",
            to seconds;

            return int;
        """

    def __seconds_to_timer_value(self):
        """
            convert the time in seconds into timer label format,
            "xx:xx";

            return string;
        """


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

        self.timer_label = TimerLabel(parent=self, text="12:23")

        self.timer_label.move(
            (Defaults.WIN_WIDTH - self.timer_label.width()) // 2 + 10,  # center on x;
            (Defaults.WIN_HEIGHT - self.timer_label.height())//2  # center on y;
        )


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
