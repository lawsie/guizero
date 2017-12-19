from guizero import *


def set_color(value):
	try:
		rgb = '#%02x%02x%02x' % (red.value, green.value, blue.value)
		coloured_text.value = rgb
		coloured_text.text_color = rgb
	except:
		print("Something went wrong with setting colours")


app = App()

title = Text(app, "Laura's awesome colour chooser", size=20, grid=[0,0])

sliderbox = Box(app, "grid")

r = Text(sliderbox, "R", grid=[1,1])
red = Slider(sliderbox, 0, 255, "horizontal", set_color, grid=[1,2])

g = Text(sliderbox, "G", grid=[2,1])
green = Slider(sliderbox, 0, 255, "horizontal", set_color, grid=[2,2])

b = Text(sliderbox, "B", grid=[3,1])
blue = Slider(sliderbox, 0, 255, "horizontal", set_color, grid=[3,2])


coloured_text = Text(app, "Coloured text", size=40, grid=[4,1])




app.display()
