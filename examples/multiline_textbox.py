from guizero import App, TextBox, PushButton

def show():
    print(textbox.value)

app = App()
textbox = TextBox(app, multiline=True, height=10, width=50, scrollbar=True, text="a multiline\ntextbox")
button = PushButton(app, text="Print", command=show)
app.display()