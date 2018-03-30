from guizero import App, PushButton, info

app = App("A picture button")

picture_button = PushButton(app, command=info, args=["button", "you push the gif"], image="guizero.gif")

picture_button_png = PushButton(app, command=info, args=["button", "you push the png"], image="guizero.png")

picture_button_jpg = PushButton(app, command=info, args=["button", "you push the jpg"], image="guizero.jpg")

app.display()