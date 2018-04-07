from guizero import App, Box, Text, TextBox, Slider, Waffle, CheckBox, Combo, Picture

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
    
def press(e):
    print("press")
    print_event_data(e)
    e.widget.bg = "red"

def release(e):
    print("release")
    print_event_data(e)
    e.widget.bg = "white"

app = App()
box = Box(app)
text = Text(box, text="events")
slider = Slider(box)
check = CheckBox(app, "check")
combo = Combo(app, ["hi", "bye"])
pic = Picture(app, image="guizero.gif")
waffle = Waffle(app)
text_box = TextBox(app)

# slider.when_left_button_pressed = press
# slider.when_left_button_released = release
# slider.when_key_pressed = press
# slider.when_key_released = release

# check.when_left_button_pressed = press
# check.when_left_button_released = release
# check.when_key_pressed = press
# check.when_key_released = release

# box.when_left_button_pressed = press
# box.when_left_button_released = release
# box.when_key_pressed = press
# box.when_key_released = release

# pic.when_left_button_pressed = press
# pic.when_left_button_released = release
# pic.when_key_pressed = press
# pic.when_key_released = release


# combo.when_left_button_pressed = press
# combo.when_left_button_released = release
# combo.when_key_pressed = press
# combo.when_key_released = release


#slider.when_clicked = clicked
#waffle.when_clicked = clicked
# waffle.when_key_pressed = key

#waffle.when_left_button_pressed = press
waffle.when_left_button_released = release
#waffle.when_mouse_over = mouse_over

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