from guizero import App, Box, PushButton
app = App()

buttons_box = Box(app, width="fill", align="bottom")
ok = PushButton(buttons_box, text="OK", align="right")
cancel = PushButton(buttons_box, text="Cancel", align="right")

app.display()
