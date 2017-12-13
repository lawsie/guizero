from guizero import App, PushButton
from time import sleep

def welcome():
    print("Welcome")

def hi():
    print("Hi")
    
def bye():
    print("Bye")

def cancel_hi():
    app.cancel(hi)

def cancel_bye():
    app.cancel(bye)

app = App()

hi_button = PushButton(app, text="Stop hi", command=cancel_hi)
bye_button = PushButton(app, text="Stop bye", command=cancel_bye)

app.after(10, welcome)

app.repeat(1000, hi)
app.repeat(1500, bye)

app.display()
