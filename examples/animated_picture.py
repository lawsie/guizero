from guizero import App, Picture, PushButton, info
app = App()

anim = Picture(app, "guizero_flash.gif")
anim.width = 200
anim.height = 100

button = PushButton(app, command=info, args=["button", "you pushed the image"], image="guizero_flash.gif")
button.width = 200
button.height = 100

app.display()