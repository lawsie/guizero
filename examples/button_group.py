from guizero import App, ButtonGroup

def selected():
    print(choice.value + " " + choice2.value)

app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], command=selected)
# You can use specific values for the button group by passing them as a 2d list.
# choice = ButtonGroup(app, options=[["cheese", "c"], ["ham", "h"], ["salad", "s"]], selected="h", command=selected)

choice2 = ButtonGroup(app, command=selected)
choice2.append("sandwich")
choice2.append("salad")

app.display()
