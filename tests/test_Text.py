import sys
from guizero import *
from guizero import events as evt

sys.path.append('../guizero')


def mouse(e):
    alerts.info(title="mouse", text = "Mouse Press")


def focus(e):
    alerts.info(title="Focus", text = "Control has focus")


def lose_focus(e):
    alerts.info(title="Lose Focus", text = "Control no longer has focus")

def key_down(e):
    alerts.info(title="Key Down", text = "Key has been pressed")


def key_up(e):
    alerts.info(title="Key Up", text = "Key has been released")


app = App("Snowman")
txt = Text(app, "Welcome to Hello world")
txt.on_mouse_press_left_button(mouse)

chb = CheckBox(app, text="Yes/No")
chb.on_mouse_press_left_button(mouse)

cob = Combo(app, options=["item 1", "Item 2"])
cob.on_mouse_move_hold_left_button(mouse)

txt1 = TextBox(app, "First Name:")
txt1.on_key_down(key_down)
txt1.on_key_up(key_up)

txt2 = TextBox(app, "Second Name:")
txt2.on_focus_in(focus)
txt2.on_focus_out(lose_focus)

app.display()

