from guizero import App, Combo

def selected(value):
    print(value)

app = App()
combo = Combo(app, ["Nothing", "Something", "Everything"], command = selected, selected="Something")
combo.remove("Something")
combo2 = Combo(app)
combo2.append("hi")
combo2.append("bye")
app.display()