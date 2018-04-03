from guizero import App, Text, TextBox

def clicked(e):
    print("clicked")
    print(e.widget)
    print(e.tk_event.type)
    print(e.mouse_x)
    print(e.mouse_x)
    print(e.key)

def key(e):
    print("key pressed")
    print(e.widget)
    print(e.tk_event.type)
    print(e.mouse_x)
    print(e.mouse_x)
    print(e.key)

def mouse_over(e):
    print("mouse over")
    print(e.widget)
    print(e.tk_event.type)
    print(e.mouse_x)
    print(e.mouse_x)
    print(e.key)

def mouse_moved(e):
    print("mouse moved")
    print(e.widget)
    print(e.tk_event.type)
    print(e.mouse_x)
    print(e.mouse_x)
    print(e.key)

def release():
    print("release")

app = App()
text = Text(app, text="hi")
text_box = TextBox(app)

app.when_clicked = clicked
app.when_key_pressed = key
app.events.set_event("<KeyRelease>", release)
# app.when_mouse_over = mouse_over
# app.when_mouse_moved = mouse_moved

# text.when_clicked = clicked
# text.when_key_pressed = key
# text.when_mouse_over = mouse_over
# text.when_mouse_moved = mouse_moved

# text_box.when_clicked = clicked
# text_box.when_key_pressed = key
# text_box.when_mouse_over = mouse_over
# text_box.when_mouse_moved = mouse_moved


app.display()