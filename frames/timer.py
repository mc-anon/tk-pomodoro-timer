import tkinter as tk
from tkinter import ttk
from collections import deque
import simpleaudio as sa


class Timer(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self["style"] = "Background.TFrame"

        self.controller = controller
        pomodoro_time = int(controller.pomodoro.get())
        self.current_time = tk.StringVar(value=f"{pomodoro_time:02d}:00")
        self.total_time = tk.StringVar(value="00:00:00")
        self.timer_running = False
        self.current_timer_label = tk.StringVar(value=controller.timer_schedule[0])
        self._timer_countdown_job = None
        self._timer_increment_job = None

        # audio
        self.pomodoro_tone = sa.WaveObject.from_wave_file('audio/pomodoro_tone.wav')
        self.short_tone = sa.WaveObject.from_wave_file('audio/short_tone.wav')
        self.long_tone = sa.WaveObject.from_wave_file('audio/long_tone.wav')

        # dynamic label
        timer_label = ttk.Label(self, textvariable=self.current_timer_label, style="LightText.TLabel")
        timer_label.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10,0))

        # settings button
        settings_btn = ttk.Button(self, text="Settings", command=show_settings, style="PomodoroButton.TButton")
        settings_btn.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))

        # timer frame including counter
        timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        timer_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")
        timer_counter = ttk.Label(timer_frame, textvariable=self.current_time, style="TimerText.TLabel")
        timer_counter.place(relx=0.5, rely=0.5, anchor="center")

        # total time frame
        total_frame = ttk.Frame(self, height="30", style="Total.TFrame")
        total_frame.grid(row=2, column=0, columnspan=2, sticky="NSEW")
        total_label = ttk.Label(total_frame, textvariable=self.total_time, style="TotalText.TLabel")
        total_label.place(relx=0.5, rely=0.5, anchor="center")

        # button frame
        btn_container = ttk.Frame(self, padding=10, style="Background.TFrame")
        btn_container.grid(row=3, column=0, columnspan=2, sticky="EW")
        btn_container.columnconfigure((0, 1, 2), weight=1)

        # start/stop buttons
        self.start_btn = ttk.Button(
                                    btn_container,
                                    text="Start",
                                    command=self.start_timer,
                                    style="PomodoroButton.TButton"
        )
        self.start_btn.grid(row=0, column=0, sticky="EW")
        self.stop_btn = ttk.Button(
                                    btn_container,
                                    text="Stop",
                                    command=self.stop_timer,
                                    state="disabled",
                                    style="PomodoroButton.TButton"
        )
        self.stop_btn.grid(row=0, column=1, sticky="EW", padx=5)

        # reset button (doesn't need 'self' as it won't be accessed outside the method)
        reset_btn = ttk.Button(
                                btn_container,
                                text="Reset",
                                command=self.reset_timer,
                                style="PomodoroButton.TButton"
        )
        reset_btn.grid(row=0, column=2, sticky="EW")

    def start_timer(self):
        self.timer_running = True
        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "enabled"
        self.countdown()
        self.total_increment()

    def stop_timer(self):
        self.timer_running = False
        self.start_btn["state"] = "enabled"
        self.stop_btn["state"] = "disabled"

        if self._timer_countdown_job:
            self.after_cancel(self._timer_countdown_job)
            self._timer_countdown_job = None

        if self._timer_increment_job:
            self.after_cancel(self._timer_increment_job)
            self._timer_increment_job = None

    def reset_timer(self):
        self.stop_timer()
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_timer_label.set(self.controller.timer_schedule[0])
        pomodoro_time = int(self.controller.pomodoro.get())
        self.current_time.set(f"{pomodoro_time:02d}:00")
        self.total_time.set("00:00:00")

    def total_increment(self):
        current_total = self.total_time.get()

        if self.timer_running:
            hours, minutes, seconds = current_total.split(":")

            if int(seconds) < 59:
                seconds = int(seconds) + 1
                minutes = int(minutes)
                hours = int(hours)
            elif int(minutes) < 59:
                seconds = 0
                minutes = int(minutes) + 1
                hours = int(hours)
            else:
                seconds = 0
                minutes = 0
                hours = int(hours) + 1

            self.total_time.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self._timer_increment_job = self.after(1000, self.total_increment)

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
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]
            self.current_timer_label.set(next_up)

            if next_up == "Pomodoro":
                self.pomodoro_tone.play()
                pomodoro_time = int(self.controller.pomodoro.get())
                self.current_time.set(f"{pomodoro_time:02d}:00")
            elif next_up == "Short Break":
                self.short_tone.play()
                short_time = int(self.controller.short_break.get())
                self.current_time.set(f"{short_time:02d}:00")
            elif next_up == "Long Break":
                self.long_tone.play()
                long_time = int(self.controller.long_break.get())
                self.current_time.set(f"{long_time:02d}:00")

            self._timer_countdown_job = self.after(1000, self.countdown)