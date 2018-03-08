from guizero import App, Picture
app = App()
picture = Picture(app, image="guizero.gif")
picture.width = 100
picture.height = 100
picture_png = Picture(app, image="guizero.png")
picture_jpg = Picture(app, image="guizero.jpg")
app.display()
