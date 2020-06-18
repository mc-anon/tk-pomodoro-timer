import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # container for all settings
        settings_container = ttk.Frame(self, padding="30 15 30 15")
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        # pomodoro label and spinbox
        pomodoro_label = ttk.Label(settings_container, text="Pomodoro: ")
        pomodoro_label.grid(row=0, column=0, sticky="W")
        pomodoro_box = tk.Spinbox(settings_container,
                                  from_=0,
                                  to=60,
                                  increment=1,
                                  textvariable=controller.pomodoro,
                                  justify="center")

        pomodoro_box.grid(row=0, column=1, sticky="EW")

        # short break label and spinbox
        sb_label = ttk.Label(settings_container, text="Short Break: ")
        sb_label.grid(row=1, column=0, sticky="W")
        sb_box = tk.Spinbox(settings_container,
                                  from_=0,
                                  to=60,
                                  increment=1,
                                  textvariable=controller.short_break,
                                  justify="center")
        sb_box.grid(row=1, column=1, sticky="EW")

        # long break label and spinbox
        lng_label = ttk.Label(settings_container, text="Long Break: ")
        lng_label.grid(row=2, column=0, sticky="W")
        lng_box = tk.Spinbox(settings_container,
                            from_=0,
                            to=60,
                            increment=1,
                            textvariable=controller.long_break,
                            justify="center")
        lng_box.grid(row=2, column=1, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=15, pady=5)
