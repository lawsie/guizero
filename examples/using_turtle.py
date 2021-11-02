from guizero import App, Drawing
from turtle import RawTurtle

app = App()
drawing = Drawing(app)
turtle = RawTurtle(drawing.tk)
turtle.forward(100)
turtle.left(720)

app.display()