from guizero import App, ButtonGroup

def selected():
    print(choice.value)
    
app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], command=selected)
#choice.value_text = "cheese"
#choice = ButtonGroup(app, options=[["cheese", "c"], ["ham", "h"], ["salad", "s"]], selected="h", command=selected)
app.display()