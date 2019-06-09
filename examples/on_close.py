from guizero import App, Text

def do_this_on_close():
    # Ask user if they really want to close the window
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

app = App()

title = Text(app, "blank app")

# When user tries to close the window, execute do_this_on_close()
app.when_closed = do_this_on_close

app.display()