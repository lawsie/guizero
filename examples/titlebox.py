from guizero import App, Text, TitleBox
app = App()
titlebox = TitleBox(app, "Title")
Text(titlebox,"Text inside a TitleBox")
app.display()
