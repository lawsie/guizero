from guizero import App, Text, PushButton

app = App(title="guizero")

intro = Text(app, text="So have a go with guizero and see what you can create.")
ok = PushButton(app, text="Ok")

app.display()