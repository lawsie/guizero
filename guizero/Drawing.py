from tkinter import Canvas, BOTH, Frame
from . import utilities as utils
from .base import Widget
from .event import EventManager

class Drawing(Widget):

    def __init__(self, master, height=100, width=100, grid=None, align=None, command=None, visible=True, enabled=None, bg=None):

        description = "[Drawing] object"

        tk = Canvas(master.tk, height=100, width=100, bd=0, highlightthickness=0)

        super(Drawing, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)


