from guizero import App, ButtonGroup

def selected():
    print(choice.value)
    
app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], command=selected)

# You want use specific values for the button group by passing them as a 2d list.
# choice = ButtonGroup(app, options=[["cheese", "c"], ["ham", "h"], ["salad", "s"]], selected="h", command=selected)

app.display()