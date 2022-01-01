from guizero import App, TextBox, Text

def filter_numbers():
    numeric_filter = filter(str.isdigit, textbox.value)
    textbox.value = "".join(numeric_filter)

app = App()
text = Text(app, text="Enter numbers only")
textbox = TextBox(app, width=40, command=filter_numbers)
app.display()