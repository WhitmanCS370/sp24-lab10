from sys import argv
from model_thread import ThreadTimerModel
from view_text import TextTimerView
from view_curse import CurseTimerView
from view_gui import GuiTimerView
from view_flask import WebTimerView

Views = {"text": CurseTimerView, "gui": GuiTimerView, "flask":WebTimerView}

if __name__ == '__main__':

    if len(argv) > 2 or (len(argv) == 2 and argv[1] not in Views.keys()):
        print("Usage: python3 timer.py [text|gui] (gui is the default)")
        exit(1)
    if len(argv) == 1:
        argv.append("gui")

    model = ThreadTimerModel()
    View = Views[argv[1]]
    View(model).run()
