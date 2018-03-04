from guizero import App, Box, Waffle, Slider, Text

def change_dim(slider):
    print("Changing size to {}x{} ".format(g_width.value, g_height.value))
    grid.width = g_width.value
    grid.height = g_height.value

app = App("Changing size")

grid = Waffle(app, width=4, height=4)

controls = Box(app, layout = "grid")

# Width
width_text = Text(controls, text="Width", grid=[0,0])
g_width = Slider(controls, start=0, end=20, command=change_dim, grid=[1,0])
g_width.value = 4

# Height
height_text = Text(controls, text="Height", grid=[0,1])
g_height = Slider(controls, start=0, end=20, command=change_dim, grid=[1,1])
g_height.value = 4

app.display()