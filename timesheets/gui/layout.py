import tkinter as tk
from tkinter import DISABLED, NORMAL
from tkinter import ttk

from datetime import timedelta


class View(tk.Frame):

    HEIGHT = 200
    WIDTH = 300

    def __init__(self, parent):
        super().__init__(parent, width=self.WIDTH, height=self.HEIGHT)

        self.__controller = None
        self.parent = parent

        self.tv_events = tv_events = ttk.Treeview(self, show='tree')
        self.lbl_worktime = lbl_worktime = ttk.Label(
            self, text="00:00", font=('Times', 40), justify="center")
        self.frm_info = frm_info = ttk.Frame(self)
        self.btn_start = btn_start = ttk.Button(
            self, text='Start', state=NORMAL,
            command=self.start_button_clicked)
        self.btn_stop = btn_stop = ttk.Button(
            self, text='Stop', state=DISABLED,
            command=self.stop_button_clicked)

        tv_events.place(relx=.05, rely=.05, relwidth=.45, relheight=.9)
        lbl_worktime.place(relx=.55, rely=.05, relwidth=.4, relheight=.35)
        frm_info.place(relx=.55, rely=.45, relwidth=.45, relheight=.2)
        btn_start.place(relx=.55, rely=.7, relwidth=.2, relheight=.2)
        btn_stop.place(relx=.75, rely=.7, relwidth=.2, relheight=.2)

        self.cap_saldo = cap_saldo = ttk.Label(
            frm_info, text="Saldo:", justify='left')
        self.cap_vacation = cap_vacation = ttk.Label(
            frm_info, text="Vacation:", justify='left')
        self.lbl_saldo = lbl_saldo = ttk.Label(
            frm_info, text="0:00 h", justify='right')
        self.lbl_vacation = lbl_vacation = ttk.Label(
            frm_info, text="0 d", justify='right')

        cap_saldo.grid(row=0, column=0, sticky='w')
        lbl_saldo.grid(row=0, column=1, sticky='w')
        cap_vacation.grid(row=1, column=0, sticky='e')
        lbl_vacation.grid(row=1, column=1, sticky='e')

    def start_button_clicked(self):
        self.btn_start['state'] = DISABLED
        self.btn_stop['state'] = NORMAL
        if self.__controller:
            self.__controller.start()

    def stop_button_clicked(self):
        self.btn_stop['state'] = DISABLED
        self.btn_start['state'] = NORMAL
        if self.__controller:
            self.__controller.stop()

    def set_controller(self, controller):
        self.__controller = controller

    def prime_timer(self, ticl_period, callback):
        if self.__controller:
            self.parent.after(ticl_period, callback)

    def set_time_worked(self, time_worked: timedelta):
        hours = time_worked.seconds//3600
        minutes = (time_worked.seconds//60) % 60
        self.lbl_worktime['text'] = f"{hours:02d}:{minutes:02d}"
