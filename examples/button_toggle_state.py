from guizero import App, PushButton
def do_start():
    print("Start button was pressed")
    startbutton.toggle()
    stopbutton.toggle()

def do_stop():
    print("Stop button was pressed")
    startbutton.toggle()
    stopbutton.toggle()

app = App()
startbutton = PushButton(app, command=do_start, text='Start')
stopbutton = PushButton(app, command=do_stop, text='Stop')
stopbutton.disable()
app.display()