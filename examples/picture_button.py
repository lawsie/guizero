from guizero import App, PushButton, info

app = App("A picture button")

picture_button = PushButton(app, command=info, args=["button", "you push the gif"])
picture_button.icon("guizero.gif")

picture_button_png = PushButton(app, command=info, args=["button", "you push the png"])
picture_button_png.icon("guizero.png")

picture_button_jpg = PushButton(app, command=info, args=["button", "you push the jpg"])
picture_button_jpg.icon("guizero.jpg")

app.display()