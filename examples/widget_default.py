from guizero import App, Text, TextBox

def reset():
    tb.bg = None
    tb.width = None
    t.height = None
    t.text_color = None
    t.font = None
    t.text_size = None
    print("\nreset to:")
    print(tb.bg)
    print(tb.width)
    print(t.height)
    print(t.text_color)
    print(t.font)
    print(t.text_size)

a = App()
t = Text(a, "widget defaults")
tb = TextBox(a)

a.after(1000, reset)

print("initial values:")
print(tb.bg)
print(tb.width)
print(t.height)
print(t.text_color)
print(t.font)
print(t.text_size)

a.bg = "red"
tb.width = 20
t.height = 5
t.text_color = "blue"
t.font = "courier new"
t.text_size = 20

print("\nchanged too:")
print(tb.bg)
print(tb.width)
print(t.height)
print(t.text_color)
print(t.font)
print(t.text_size)

a.display()