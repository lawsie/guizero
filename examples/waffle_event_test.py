from guizero import App, Waffle

def w_click():
    print("w_click")

def click():
    print("click")

a = App()
w = Waffle(a)
w.when_clicked = click
a.display()