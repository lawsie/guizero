from guizero import App, ButtonGroup

def selected():
    print(choice.value)

app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], selected=1, command=selected)
app.display()