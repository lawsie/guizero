from guizero import App, LabelBox, Text
app = App()
labelbox = LabelBox(app, "Label box")
Text(labelbox,"Text inside a LabelBox")

labelbox2 = LabelBox(app)
Text(labelbox2, "This LabelBox has no label")
app.display()
