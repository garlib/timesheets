import tkinter as tk

from timesheets.gui.layout import View
from timesheets.gui.controller import Controller


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Timesheets")
        self.resizable(0, 0)

        self.view = View(self)
        self.view.pack()

        self.controller = Controller(self.view, None)
        self.view.set_controller(self.controller)
