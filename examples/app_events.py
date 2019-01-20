from guizero import App, Text, TextBox, Slider, Waffle, CheckBox, info

def intro():
    info("events", "this is all about events")

# when return is pressed back the test red and then turn it back to black
def key_pressed(e):

    def text_color_black():
        text_box.text_color = "black"

    # return pressed
    if ord(e.key) == 13:
        e.widget.text_color = "red"
        e.widget.after(1000, text_color_black)

def mouse_enters(e):
    e.widget.bg = "lightblue"

def mouse_leaves(e):
    e.widget.bg = "white"

def right_pressed():
    waffle.set_pixel(0,0,"green")

def right_released():
    waffle.set_pixel(0,0,"grey")

app = App()
text = Text(app, text="events")
slider = Slider(app)
text_box = TextBox(app)
check = CheckBox(app, "check")
waffle = Waffle(app)

# when clicked
text.when_clicked = intro

# when key pressed
text_box.when_key_pressed = key_pressed

# highlight widget when move over
check.when_mouse_enters = mouse_enters
check.when_mouse_leaves = mouse_leaves
slider.when_mouse_enters = mouse_enters
slider.when_mouse_leaves = mouse_leaves
text_box.when_mouse_enters = mouse_enters
text_box.when_mouse_leaves = mouse_leaves
waffle.when_mouse_enters = mouse_enters
waffle.when_mouse_leaves = mouse_leaves

# right button pressed and released
waffle.when_right_button_pressed = right_pressed
waffle.when_right_button_released = right_released

app.display()
