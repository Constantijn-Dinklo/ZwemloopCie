from datetime import timedelta
from PySide6 import QtWidgets, QtCore

from clock import Clock
import time

import threading

class TimeScreen(QtWidgets.QWidget):

    def __init__(self, clock: Clock):
        super().__init__()

        self.clock = clock

        self.time_text = QtWidgets.QLabel("")
        self.time_text.setStyleSheet(''' font-size: 450px; ''')

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.time_text)

        time_display_thread = threading.Thread(target=self.updateTime)
        time_display_thread.start()
        
    def updateTime(self):
        while True:
            time_dif: timedelta = self.clock.elapsedTime()

            hours, remainder = divmod(time_dif.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_dif_text = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
            self.time_text.setText(time_dif_text)
            time.sleep(1)

