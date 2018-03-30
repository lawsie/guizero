from guizero import App, PushButton, Slider, info

def resize():
    button.width = width.value
    button.height = height.value

app = App()
button = PushButton(app, image="guizero.gif", command=info, args=["button", "you push the button"])

width = Slider(app, start = 10, end = button.width, command = resize)
width.value = button.width

height = Slider(app, start = 10, end = button.height, command = resize)
height.value = button.height

app.display()
