from guizero import App, TextBox, PushButton, Box, Combo, CheckBox

def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()

def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)

def change_font():
    editor.font = font.value

def change_text_size():
    text_sizes = {"small": 6, "medium": 10, "large": 14}
    editor.text_size = text_sizes[size.value]
    # resize the widget because if the text is made bigger, it needs to be repacked,
    # and if you dont size it differently first tkinter wont repack it 
    editor.resize(1, 1)
    editor.resize("fill", "fill")

def change_theme():
    if dark_theme.value:
        app.bg = "black"
        app.text_color = "white"
    else:
        app.bg = None
        app.text_color = None
        
app = App(title="textzero")

file_controls = Box(app, align="top", width="fill", border=True)
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")
save_button = PushButton(file_controls, text="Save", command=save_file, align="right")
open_button = PushButton(file_controls, text="Open", command=open_file, align="right")

editor = TextBox(app, multiline=True, height="fill", width="fill")

preferences_controls = Box(app, align="bottom", width="fill", border=True)
font = Combo(preferences_controls, options=["courier", "times new roman", "verdana"], align="left", command=change_font)
size = Combo(preferences_controls, options=["small", "medium", "large"], align="left", command=change_text_size)
dark_theme = CheckBox(preferences_controls, text="dark", align="left", command=change_theme)

app.display()