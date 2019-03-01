from guizero import App, Text, Box, Drawing, Slider, PushButton, Combo

def start_paint(event):
    painting.last_event = event

def stop_paint():
    painting.last_event = None
    painting.last_shape = None

def draw_paint(event):
    if tool.value == "line":
        painting.line(
            painting.last_event.x, painting.last_event.y, 
            event.x, event.y, 
            color=(red.value, green.value, blue.value), 
            width=line_width.value)

        painting.last_event = event
    else:
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        
        if tool.value == "rectangle":
            painting.last_shape = painting.rectangle(
                painting.last_event.x, painting.last_event.y, 
                event.x, event.y, 
                color=(red.value, green.value, blue.value)
            )
        elif tool.value == "oval":
            painting.last_shape = painting.oval(
                painting.last_event.x, painting.last_event.y, 
                event.x, event.y, 
                color=(red.value, green.value, blue.value)
            )

def update_color():
    color_label.bg = (red.value, green.value, blue.value)
    color_label.text_color = (255 - red.value, 255 - green.value, 255 - blue.value)

def select_tool():
    line_width_box.visible = tool.value == "line"
    
a = App(title="Paintzero")

tool_box = Box(a, height="fill", border=True, align="left")
paint_box = Box(a, width="fill", height="fill", border=True, align="right")

tool = Combo(tool_box, options=["line", "rectangle", "oval"], selected="line", align="top", width="fill", command=select_tool)

color_label = Text(tool_box, text="color", align="top", width="fill")
color_label.bg = "black"
color_label.text_color = "white"

red = Slider(tool_box, end=255, command=update_color)
red.bg = (255, 0, 0)

green = Slider(tool_box, end=255, command=update_color)
green.bg = (0, 255, 0)

blue = Slider(tool_box, end=255, command=update_color)
blue.bg = (0, 0, 255)

line_width_box = Box(tool_box, align="top")
Text(line_width_box, text="width", align="top")
line_width = Slider(line_width_box, start=1, end=10, align="top")

painting = Drawing(paint_box, width="fill", height="fill")
painting.last_event = None
painting.last_shape = None
painting.when_left_button_pressed = start_paint
painting.when_mouse_dragged = draw_paint
painting.when_left_button_released = stop_paint

PushButton(tool_box, text="Clear", command=painting.clear, align="bottom", width="fill")

a.display()