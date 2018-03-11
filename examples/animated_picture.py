from guizero import App, Picture, PushButton, info
app = App()

anim = Picture(app, "banana.gif")
anim.width = 200
anim.height = 200

button = PushButton(app, command=info, args=["button", "you pushed the banana"], image="banana.gif")
button.width = 200
button.height = 200

app.display()