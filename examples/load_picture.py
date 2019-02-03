from guizero import App, Picture

app = App()
picture = Picture(app, image="guizero.gif")
picture_png = Picture(app, image="guizero.png")
picture_jpg = Picture(app, image="guizero.jpg")

app.display()
