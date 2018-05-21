from guizero import App, Text, TextBox

def reset():
    t.enable()
    tb.bg = None

a = App()
t = Text(a, "widget defaults")
tb = TextBox(a)
a.bg = "red"
a.after(1000, reset)
#a.set_tk_config(["bg"], None)
#tb.set_tk_config(["bg"], None)
t.text_color = "blue"
t.disable()
print(t.enabled)
a.display()