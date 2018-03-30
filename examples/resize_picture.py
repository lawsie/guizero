from guizero import App, Picture, Slider

def resize():
    picture.width = width.value
    picture.height = height.value

app = App()
picture = Picture(app, image="guizero.gif")

width = Slider(app, start = 10, end = picture.width, command = resize)
width.value = picture.width

height = Slider(app, start = 10, end = picture.height, command = resize)
height.value = picture.height

app.display()
