from guizero import App, Text, PushButton

def show_button_state():
    if button.value:
        button_state.value = "pressed"
    else:
        button_state.value = "released"

app = App()
button = PushButton(app)
button_state = Text(app)
# continually update the button state
app.repeat(50, show_button_state)
app.display()
