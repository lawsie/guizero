from guizero import App, PushButton
def pressed():
    print("button was pressed")

def message(msg):
    print(msg)
    
app = App()
button = PushButton(app, command=pressed, text='Press me')
button_with_args = PushButton(app, command=message, text='Say Hi', args=["hi"])
app.display()