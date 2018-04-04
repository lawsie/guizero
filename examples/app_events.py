from guizero import App, Text, TextBox

def clicked(e):
    print("clicked")
    print(e.widget)
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.key)

def key(e):
    print("key pressed")
    print(e.widget)
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.display_x)
    print(e.display_y)
    print(e.key)

def mouse_over(e):
    print("mouse over")
    print(e.widget)
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.key)

def mouse_moved(e):
    print("mouse moved")
    print(e.widget)
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.display_x)
    print(e.display_y)
    print(e.key)


def mouse_dragged(e):
    print("mouse dragged")
    print(e.widget)
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.display_x)
    print(e.display_y)
    print(e.key)

def press():
    print("press")

def release():
    print("release")

app = App()
text = Text(app, text="hi")
text_box = TextBox(app)

app.when_mouse_dragged = mouse_dragged

#app.when_key_pressed = key
#app.events.set_event("<KeyRelease>", release)
# app.events.set_event("<ButtonPress-1>", press)
# app.events.set_event("<ButtonRelease-1>", release)
# app.when_mouse_over = mouse_over
# app.when_mouse_moved = mouse_moved

# app.when_left_button_pressed = press
# app.when_left_button_released = release

# app.when_right_button_pressed = press
# app.when_right_button_released = release

# app.when_key_pressed = press
# app.when_key_released = release

# text.when_clicked = clicked
# text.when_key_pressed = key
# text.when_mouse_over = mouse_over
# text.when_mouse_moved = mouse_moved

# text_box.when_clicked = clicked
# text_box.when_key_pressed = key
# text_box.when_mouse_over = mouse_over
# text_box.when_mouse_moved = mouse_moved


app.display()