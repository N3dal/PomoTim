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

# wipe the terminal screen;
Defaults.clear()


class MainWindow(QMainWindow):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
