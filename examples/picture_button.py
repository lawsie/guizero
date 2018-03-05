from guizero import App, PushButton, info

app = App("A picture button")
picture_button = PushButton(app, command=info, args=["button", "you push the picture button"])
picture_button.icon("guizero.jpg")
app.display()