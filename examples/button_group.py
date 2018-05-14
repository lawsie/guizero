from guizero import App, ButtonGroup

def selected():
    print(choice.value)
    
app = App()
app.bg = "green"
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], command=selected)

# ButtonGroup values are integers, if you want use specific values you can specify them on the constructor
# choice = ButtonGroup(app, options=[["cheese", "c"], ["ham", "h"], ["salad", "s"]], selected="h", command=selected)

app.display()