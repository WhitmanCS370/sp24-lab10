from flask import Flask, render_template, request
from controller import TimerController, TimerView
import model_thread
import pygame

app = Flask(__name__)

class WebTimerView(TimerView):
    """A web-based timer application."""

    def __init__(self, model):
        """Set up application state."""
        self.controller = TimerController(model, self)
        self.minutes = 0
        self.seconds = 0
        self.sound_file = None

    def run(self):
        """Run the application."""
        app.run()

    @app.route("/")
    def index(self):
        """Render the timer page."""
        return render_template("timer.html", minutes=self.minutes, seconds=self.seconds)

    @app.route("/start", methods=["POST"])
    def start(self):
        """Start the timer."""
        time_in_seconds = 60 * self.minutes + self.seconds
        self.controller.start(time_in_seconds)
        return ""

    @app.route("/stop", methods=["POST"])
    def stop(self):
        """Stop the timer."""
        self.controller.stop()
        return ""

    @app.route("/pause", methods=["POST"])
    def pause(self):
        """Pause the timer."""
        self.controller.pause()
        return ""

    @app.route("/select_sound", methods=["POST"])
    def select_sound(self):
        """Select a sound file to play when the timer is done."""
        self.sound_file = request.files["sound_file"]
        return ""

    def update_time(self, time_in_seconds):
        """Update the time stored by this object. Called by the controller."""
        self.minutes = time_in_seconds // 60
        self.seconds = time_in_seconds % 60

    def timer_done(self):
        """Indicate the timer is done. Called by the controller."""
        if self.sound_file:
            pygame.mixer.init()
            pygame.mixer.music.load(self.sound_file)
            pygame.mixer.music.play()

if __name__ == "__main__":
    model = timer_thread.ThreadTimerModel()
    WebTimerView().run()