from tkinter import Canvas, ALL
from . import utilities as utils


class Painter:
    def __init__(self,master,width=100,height=100,background='white',grid=None,align=None):

        self.tk = Canvas(master.tk,width=width,height=height,background=background)
        self._height = height
        self._width = width
        
        utils.auto_pack(self,master,grid,align)

    def draw_line(self,x1,y1,x2,y2,color='black'):
        self.tk.create_line(x1,y1,x2,y2,fill=color)

    def draw_ellipse(self,x,y,width,height,color=''):
        self.tk.create_oval(x,y,x+width,y+height,fill=color)

    def draw_rectangle(self,x,y,width,height,color=''):
        self.tk.create_rectangle(x,y,x+width,y+height,fill=color)

    def clear(self):
        self.tk.delete(ALL)

        
