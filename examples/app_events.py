from guizero import App, Text, TextBox, Slider, Waffle

def print_event_data(e):
    print(e.tk_event.type)
    print(e.x)
    print(e.y)
    print(e.display_x)
    print(e.display_y)
    print(e.key)

def clicked(e):
    print("clicked")
    print_event_data(e)
    
def key(e):
    print("key pressed")
    print_event_data(e)
    
def mouse_over(e):
    print("mouse over")
    print_event_data(e)
    
def mouse_moved(e):
    print("mouse moved")
    print_event_data(e)
    
def mouse_dragged(e):
    print("mouse dragged")
    print_event_data(e)
    
def press():
    print("press")
    print_event_data(e)

def release():
    print("release")
    print_event_data(e)

app = App()
text = Text(app, text="hi")
slider = Slider(app)
waffle = Waffle(app)

text_box = TextBox(app)

#slider.when_clicked = clicked
waffle.when_clicked = clicked
waffle.when_key_pressed = key

# app.when_clicked = clicked
# app.events.set_event("myclick", "<Button-1>", press)


# app.when_key_pressed = key
# app.events.set_event("<KeyRelease>", release)
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