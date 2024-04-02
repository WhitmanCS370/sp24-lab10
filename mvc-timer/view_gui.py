import tkinter as tk
from tkinter import ttk
import winsound
from abc import ABC, abstractmethod
from controller import TimerController, TimerView

# Fixed up from AI generated code
# See https://chat.openai.com/share/35e48a9c-ba3f-461e-bc01-633ef4343eff


class SoundPlayer:
    """
    Plays a sound based on the input.
    Input: sound (int) - 0, 1, or 2
    - 0: single beep
    - 1: double beep
    - 2: triple beep
    """
    def __init__(self, sound):
        if sound not in [0, 1, 2]:
            raise ValueError("Invalid sound specified. Please use 0, 1, or 2.")
        self.sound = sound

    def __call__(self):
        # Use the play method when the instance is called.
        self.play(self.sound)

    def play(self, sound):
        # Play the sound according to the specified number of beeps.
        for _ in range(sound + 1):
            winsound.Beep(1000, 1000)

class GuiTimerView(TimerView):
    """A graphical timer application."""

    def __init__(self, model):
        """Set up application window and other state."""

        self.controller = TimerController(model, self)
        self.minutes = 0    # Must be non-negative
        self.seconds = 0    # Must be in the range 0..59, inclusive

        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        
        self.timer_label = ttk.Label(self.root, text="00:00", font=("Helvetica", "36"))
        self.timer_label.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        
        self.minutes_up_button = ttk.Button(self.root, text="▲", command=self.increment_minutes)
        self.minutes_up_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.minutes_down_button = ttk.Button(self.root, text="▼", command=self.decrement_minutes)
        self.minutes_down_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.seconds_up_button = ttk.Button(self.root, text="▲", command=self.increment_seconds)
        self.seconds_up_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.seconds_down_button = ttk.Button(self.root, text="▼", command=self.decrement_seconds)
        self.seconds_down_button.grid(row=1, column=2, padx=5, pady=5)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start)
        self.start_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop, state="disabled")
        self.stop_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause, state="disabled")
        self.pause_button.grid(row=2, column=2, padx=5, pady=5)

        self.select_sound = ttk.Combobox(self.root, values=["Beep", "Double Beep", "Triple Beep"])
        self.select_sound.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def play_sound(self, player):
        """Play the selected sound using the provided SoundPlayer instance."""
        sound = self.select_sound.get()
        sound_mapping = {"Beep": 0, "Double Beep": 1, "Triple Beep": 2}
        if sound in sound_mapping:
            sound_code = sound_mapping[sound]
            player_instance = player(sound_code)
            player_instance()  # This calls the __call__ method of SoundPlayer.

        
    def run(self):
        """Run the application."""
        self.root.mainloop()

    def quit(self):
        """Quit the application."""
        self.controller.stop()
        self.root.destroy()

    def increment_minutes(self):
        """Increment minutes by 1. Called on minutes up button press."""
        self.minutes += 1
        self.display_time()
        
    def decrement_minutes(self):
        """Decrement minutes by 1. Called on minutes down button press."""
        if self.minutes > 0:
            self.minutes -= 1
            self.display_time()
        
    def increment_seconds(self):
        """Increment seconds by 5. Called on seconds up button press."""
        self.seconds += 5
        self.seconds %= 60
        self.display_time()
        
    def decrement_seconds(self):
        """Decrement seconds by 5. Called on seconds down button press."""
        self.seconds -= 5
        self.seconds %= 60
        self.display_time()
        
    def display_time(self):
        """Display the time stored by this object."""
        time_str = f"{self.minutes:02d}:{self.seconds:02d}"
        self.timer_label.config(text=time_str)

    def update_time(self, time_in_seconds):
        """Update the time stored by this object. Called by the controller."""
        self.minutes = time_in_seconds // 60
        self.seconds = time_in_seconds % 60
        self.display_time()

    def timer_done(self):
        """Indicate the timer is done. Called by the controller.""" 
        self.play_sound(SoundPlayer) # Now I have to pass arguments to the SoundPlayer class here, which defeats the purpose of the whole injection
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.pause_button.config(state="disabled")
        
    def start(self):
        """Start the timer."""
        time_in_seconds = 60*self.minutes + self.seconds
        self.controller.start(time_in_seconds)
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.pause_button.config(state="normal")
        
    def stop(self):
        """Stop the timer."""
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.pause_button.config(text="Pause", state="disabled")
        self.minutes = 0
        self.seconds = 0
        self.display_time()
        self.controller.stop()
        
    def pause(self):
        """Pause the timer, or resume if already paused.."""
        if self.controller.paused():
            self.controller.resume()
            self.pause_button.config(text="Pause")
        else:
            self.controller.pause()
            self.pause_button.config(text="Resume")

if __name__ == "__main__":
    GuiTimerView().run()
