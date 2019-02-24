from guizero import App, Drawing

a = App()
d = Drawing(a)
d.tk.create_rectangle(0,0,50,50,fill="blue")
a.display()
