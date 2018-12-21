from guizero import App, PushButton, TextBox

def welcome():
    print("Welcome")

def hi():
    print("Hi")

def message(my_message):
    print(my_message)

def whatever():
    # say whatever using the message function, passing the text as an argument
    app.after(200, message, args=["Whatever"])

def cancel_hi():
    app.cancel(hi)

app = App()

# create some buttons
hi_button = PushButton(app, cancel_hi, text="Stop hi")
what_button = PushButton(app, whatever, text="Whatever")

# after a very short pause, say welcome
app.after(10, welcome)

# keep repeating hi, until it is cancelled
app.repeat(1000, hi)

app.display()
