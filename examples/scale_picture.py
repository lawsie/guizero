from guizero import App, Slider, Picture

def resize():
    picture.resize(width.value, height.value)

app = App(layout="grid", width=550, height=200)

picture = Picture(app, image="guizero.gif", grid=[0,1])

width = Slider(app, command=resize, grid=[0,0], start=1, end=picture.width)
width.width = picture.width
width.value = picture.width

height = Slider(app, command=resize, horizontal=False, grid=[1,1], start=1, end=picture.height)
height.height = picture.height
height.value = picture.height

app.display()
