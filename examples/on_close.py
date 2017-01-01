from guizero import *

"""
Functions
"""
# Ask user if they really want to close the window
def do_this_on_close():
    if alerts.yesno("Close", "Do you want to quit?"):
        app.destroy()

"""
Main
"""
app = App()

title = Text(app, "blank app")

# When user tries to close the window, execute do_this_on_close()
app.on_close(do_this_on_close)

app.display()
