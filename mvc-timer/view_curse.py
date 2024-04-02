import curses
from threading import Thread
from time import sleep
from controller import TimerController, TimerView
from pygame import mixer


class CurseTimerView(TimerView):

    def __init__(self, model):
        self._controller = TimerController(model, self)
        self.stdscr = curses.initscr()

    def run(self):
        """Run the text-based timer."""
        time = self._getTimeFromUser()
        self._thread = Thread(target=self._input_loop, daemon=True)
        self._thread.start()
        self._controller.start(time)
        while not self._controller.stopped():
            sleep(1)

    def update_time(self, time):
        """Display the time."""
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, f"Time remaining: {time} seconds")
        self.stdscr.refresh()

    def timer_done(self):
        """Indicate the timer is done."""
        mixer.init()
        mixer.music.load("endsound.mp3")
        mixer.music.play()
        self.stdscr.clear()
        self.stdscr.addstr(1, 0, "DING DING DING DING DING")
        self.stdscr.refresh()
        self.stdscr.clear()

    def _getTimeFromUser(self):
        """Get a positive integer time from the user."""
        while True:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Enter time in seconds: ")
            self.stdscr.refresh()
            s = self.stdscr.getstr().decode()
            if s.startswith('q'):
                return
            try:
                time = int(s)
                assert time >= 0
                return time
            except:
                continue

    def _input_loop(self):
        """Accept user input to pause or resume. Run in a new thread."""
        self.stdscr.addstr(1, 0, "Hit return to pause or resume timer")
        self.stdscr.refresh()
        while True:
            key = self.stdscr.getch()
            if key == ord('\n'):
                self.stdscr.addstr(2, 0, "Paused")
                self.stdscr.refresh()
                self._controller.pause()
                self.stdscr.getch()
                self._controller.resume()

# def main(stdscr):
#     stdscr.clear()
#     view = TextTimerView(model, stdscr)
#     view.run()

if __name__ == "__main__":
    curses.wrapper(main)
