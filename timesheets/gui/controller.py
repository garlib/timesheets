import threading
from timesheets.gui.layout import View

from datetime import datetime, timedelta


class Controller:

    def __init__(self, view: View, model):
        self.view = view
        self.model = model
        self.tick_period = 1_000
        self.__running = False
        self.__lock_timer = threading.Lock()
        self.__time_start = None
        self.__time_stop = None

    def start(self):
        self.__time_start = datetime.now()  # TODO move to model

        self.__lock_timer.acquire()
        try:
            self.__running = True
            self.view.prime_timer(self.tick_period, self.tick)

        finally:
            self.__lock_timer.release()

    def stop(self):
        self.__time_stop = datetime.now()  # TODO move to model

        self.__lock_timer.acquire()
        self.__running = False
        self.__lock_timer.release()

    def tick(self):
        now = datetime.now()
        time_worked = now - self.__time_start
        self.view.set_time_worked(time_worked)

        self.__lock_timer.acquire()
        try:
            if self.__running:
                self.view.prime_timer(self.tick_period, self.tick)

        finally:
            self.__lock_timer.release()
