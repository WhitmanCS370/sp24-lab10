from abc import ABC, abstractmethod
from pygame import mixer

class TimerView(ABC):
    """Displays the timer."""

    @abstractmethod
    def run(self):
        """Called by a client to run the view."""
        pass
    
    @abstractmethod
    def update_time(self):
        """Called by the controller when the timer value may have changed."""
        pass

    @abstractmethod
    def timer_done(self):
        """Called by the controller when the timer reaches 0."""
        pass

    def done_sound(self, file='bell.wav'):
        mixer.init()
        sound=mixer.Sound(file)
        sound.play()

class TimerModel(ABC):
    """
    Models a timer.
    """

    @abstractmethod
    def __init__(self):
        """Initialize the timer."""
        pass

    @property 
    def time(self):
        """Get current time in seconds."""
        return 0

    @time.setter
    def time(self, value):
        """Set current time to the given non-negative value in seconds."""
        pass

    @property 
    def running(self):
        """True if the timer is running"""
        return False

    @abstractmethod
    def start_timer(self):
        """Start the timer from the current time."""
        pass

    @abstractmethod
    def stop_timer(self):
        """Stop the timer, retaining the current time."""
        pass
