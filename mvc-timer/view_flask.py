from flask import Flask, render_template, request
from controller import TimerController, TimerView

app = Flask(__name__)

class WebTimerView(TimerView):
    """A web-based timer application."""

    def __init__(self, model):
        self.controller = TimerController(model, self)
        self.minutes = 0
        self.seconds = 0

    def update_time(self, time_in_seconds):
        self.minutes = time_in_seconds // 60
        self.seconds = time_in_seconds % 60

    def timer_done(self):
        pass

    # def run(self):
    #     pass

@app.route('/', methods=['GET', 'POST'])
def index():
    timer_view = WebTimerView()
    if request.method == 'POST':
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])
        time_in_seconds = 60 * minutes + seconds
        timer_view.controller.start(time_in_seconds)
    return render_template('index.html', timer=timer_view)

if __name__ == "__main__":
    app.run(debug=True)
