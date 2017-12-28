from guizero import App, Text, PushButton, ButtonGroup, Picture, info, warn

def change_message(message):
    message_text.value = message

# these functions are called in order based on the users actions
def message1():
    change_message("guizero makes creating GUI's easy")
    app.after(2000, message2)

def message2():
    message = "guizero uses events to make things happen\n" 
    message += "events are actions, like clicking a push button\n"
    message += "so...  create an event!"
    change_message(message)
    app.after(1000, show_the_button)

def show_the_button():
    button.show()

def clicked_the_button():
    button.hide()
    change_message("well done, you created an event by clicking the button")
    app.after(2000, message3)

def message3():
    message = "events are any action the user takes in your app\n"
    message += "choose carefully"
    change_message(message)
    app.after(1000, show_the_selection)

def show_the_selection():
    selection.show()

def selection_chosen():
    selection.hide()
    if selection.value == "1":
        info("well done", "you chose wisely")
        goodbye()
    else:
        warn("arrrgh", "next time, choose wisely!")
        app.after(2000, show_the_selection)

def goodbye():
    change_message("Thanks")
    logo.show()

# create the app and the widgets
app = App()
message_text = Text(app, text = "Welcome to guizero")
button = PushButton(app, clicked_the_button, text = "Click me")
button.hide()
selection = ButtonGroup(app, selected = 0, command = selection_chosen, options = ["choose me", "don't choose me"])
selection.hide()
logo = Picture(app, "guizero.gif")
logo.hide()

# show the first message after 2 seconds
app.after(2000, message1)

app.display()

