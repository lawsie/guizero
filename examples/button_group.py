from guizero import App, ButtonGroup
app = App()
choice = ButtonGroup(app, options=["cheese", "ham", "salad"], selected=1)
app.display()