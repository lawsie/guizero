from guizero import App, PushButton, question, Text

def button_pressed():
    name = question("Hello", "What's your name?")
    # if Cancel is pressed None is return
    # so check a name was entered
    if name is not None:
        hello.value = "Hello " + name

app = App()
button = PushButton(app, command=button_pressed, text="Hello")
hello = Text(app)
app.display()