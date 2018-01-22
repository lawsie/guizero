from guizero import App, Combo

def selected(value):
    print(value)

app = App()
combo = Combo(app, ["Nothing", "Something"], command = selected)
combo.add_option("Everything")

app.display()