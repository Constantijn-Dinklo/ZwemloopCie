from datetime import datetime

class Clock:


    def __init__(self):
        self.start_time = datetime.now()

    def startClock(self):
        self.start_time = datetime.now()

    def getStartTime(self):
        return self.start_time

    def elapsedTime(self):
        now = datetime.now()
        time_diff = now - self.start_time

        return time_diff
