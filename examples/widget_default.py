from guizero import App, Text, TextBox, Slider, PushButton

def reset():
    # tb.bg = None
    # tb.width = None
    # t.height = None
    # t.text_color = None
    # t.font = None
    # t.text_size = None
    # s.width = None
    p.width = None
    pb.width = None
    p.height = None
    pb.height = None
    
    print("\nreset to:")
    # print(tb.bg)
    # print(tb.width)
    # print(t.height)
    # print(t.text_color)
    # print(t.font)
    # print(t.text_size)
    # print(s.width)
    print(p.width)
    print(pb.width)
    print(p.height)
    print(pb.height)
    

a = App()
t = Text(a, "widget defaults")
tb = TextBox(a)
s = Slider(a)
p = PushButton(a)
pb = PushButton(a, image="guizero.gif")

a.after(1000, reset)

print("initial values:")
# print(tb.bg)
# print(tb.width)
# print(t.height)
# print(t.text_color)
# print(t.font)
# print(t.text_size)
# print(s.width)
print(p.width)
print(pb.width)
print(p.height)
print(pb.height)
    

# a.bg = "red"
# tb.width = 20
# t.height = 5
# t.text_color = "blue"
# t.font = "courier new"
# t.text_size = 20
# s.width = 150
p.width = 20
pb.width = 100
p.height = 20
pb.height = 100

print("\nchanged too:")
# print(tb.bg)
# print(tb.width)
# print(t.height)
# print(t.text_color)
# print(t.font)
# print(t.text_size)
# print(s.width)
print(p.width)
print(pb.width)
print(p.height)
print(pb.height)

a.display()