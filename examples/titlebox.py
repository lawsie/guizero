from guizero import App, Text, TitleBox
app = App()

titlebox = TitleBox(app, "Title of the box")

# change properties
# titlebox.text_size = 15
# titlebox.font = "courier new"
# titlebox.text_color = "red"

message = Text(titlebox,"Text inside a TitleBox")

app.display()
