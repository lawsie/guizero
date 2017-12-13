from guizero import App, PushButton, TextBox
from time import sleep

def welcome():
    print("Welcome")

def hi():
    print("Hi")
    
def bye():
    print("Bye")

def message(my_message):
    print(my_message)

def cancel_hi():
    app.cancel(hi)

def cancel_bye():
    app.cancel(bye)

app = App()

# create some buttons 
hi_button = PushButton(app, cancel_hi, text="Stop hi")
bye_button = PushButton(app, cancel_bye, text="Stop bye")
what_button = PushButton(app, app.after, text="Whatever", args=(1000, message, "whatever",))

app.after(10, welcome)

app.repeat(1000, hi)
app.repeat(1500, bye)

app.display()
