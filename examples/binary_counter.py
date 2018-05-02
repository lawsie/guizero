from guizero import App, Text

number = 0
base = 2

def to_str(n,base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base,base) + convert_string[n%base]

def counter():
    global number
    number = number + 1
    binary.value = str(to_str(number, base)).zfill(5)
    denary.value = str(number).zfill(5)

app = App()
denary = Text(app, text="00000", size=100)
binary = Text(app, text="00000", size=100)

denary.width = 10
binary.width = 10

denary.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()