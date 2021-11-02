from guizero import App, Text

def double_click():
    double_click_me.value = "Thanks"
    app.after(1000, reset)

def reset():
    double_click_me.value ="Double click me"

app = App()

double_click_me = Text(app, text="Double click me")
double_click_me.when_double_clicked = double_click

app.display()