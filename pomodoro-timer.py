import tkinter as tk
from tkinter import ttk
from collections import deque


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title = "Pomodoro Timer"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(container)
        timer_frame.grid(sticky="NSEW")


class Timer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.current_time = tk.StringVar(value="00:10")
        self.timer_running = False
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        self.current_timer_label = tk.StringVar(value=self.timer_schedule[0])
        self._timer_countdown_job = None

        # dynamic label
        timer_label = ttk.Label(self, textvariable=self.current_timer_label)
        timer_label.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10,0))

        # timer frame including counter
        timer_frame = ttk.Frame(self, height="100")
        timer_frame.grid(row=1, column=0, pady=(10, 0), sticky="NSEW")
        timer_counter = ttk.Label(timer_frame, textvariable=self.current_time)
        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

        # button frame
        btn_container = ttk.Frame(self, padding=10)
        btn_container.grid(row=2, column=0, sticky="EW")
        btn_container.columnconfigure((0, 1, 2), weight=1)

        # start/stop buttons
        self.start_btn = ttk.Button(btn_container,
                               text="Start",
                               command=self.start_timer)
        self.start_btn.grid(row=0, column=0, sticky="EW")
        self.stop_btn = ttk.Button(btn_container,
                              text="Stop",
                              command=self.stop_timer,
                              state="disabled")
        self.stop_btn.grid(row=0, column=1, sticky="EW", padx=5)

        # reset button (doesn't need 'self' as it won't be accessed outside the method)
        reset_btn = ttk.Button(btn_container,
                                    text="Reset",
                                    command=self.reset_timer)
        reset_btn.grid(row=0, column=2, sticky="EW")

    def start_timer(self):
        self.timer_running = True
        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "enabled"
        self.countdown()

    def stop_timer(self):
        self.timer_running = False
        self.start_btn["state"] = "enabled"
        self.stop_btn["state"] = "disabled"

        if self._timer_countdown_job:
            self.after_cancel(self._timer_countdown_job)
            self._timer_countdown_job = None

    def reset_timer(self):
        self.stop_timer()
        self.timer_schedule = deque(self.timer_order)
        self.current_timer_label.set(self.timer_schedule[0])
        self.current_time.set("25:00")

    def countdown(self):
        current_time = self.current_time.get()

        if self.timer_running and current_time != "00:00":
            minutes, seconds = current_time.split(":")

            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)
            else:
                seconds = 59
                minutes = int(minutes) - 1

            self.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self._timer_countdown_job = self.after(1000, self.countdown)

        elif self.timer_running and current_time == "00:00":
            self.timer_schedule.rotate(-1)
            next_up = self.timer_schedule[0]
            self.current_timer_label.set(next_up)

            if next_up == "Pomodoro":
                self.current_time.set("25:00")
            elif next_up == "Short Break":
                self.current_time.set("05:00")
            elif next_up == "Long Break":
                self.current_time.set("10:00")

            self._timer_countdown_job = self.after(1000, self.countdown)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()