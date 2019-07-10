## Events

Custom events can be added to guizero widgets to call functions when the user takes the following actions:

- when clicked - `when_clicked`
- when the left mouse button is pressed - `when_left_button_pressed`
- when the left mouse button is released - `when_left_button_released`
- when the right mouse button is pressed - `when_right_button_pressed`
- when the right mouse button is released - `when_right_button_released`
- when a key is pressed - `when_key_pressed`
- when a key is released - `when_key_released`
- when the mouse enters a widget - `when_mouse_enters`
- when the mouse leaves a widget - `when_mouse_leaves`
- when the mouse is dragged across a widget - `when_mouse_dragged`

Events are set by assigning them to a function:

```python
def do_this():
    print("The widget was clicked")

widget.when_clicked = do_this
```

### Event Data

The function which is called can also accept a parameter and will be passed data about the event which occured.

The event data returned has:

- `widget` - the guizero widget which raised the event
- `tk_event` - the [tkinter event object](http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm)
- `key` - the key which raised the event
- `x` - the mouse's x position relative to the widget when the event occured
- `y` - the mouse's y position relative to the widget when the event occured
- `display_x` - the mouse's x position on the display when the event occured
- `display_y` - the mouse's y position on the display when the event occured

```python
def clicked(event_data):
    print("widget clicked = " + event_data.widget)
    print("mouse position = " + event_data.x + "." + event_data.y)

widget.when_clicked = clicked
```

### Example

Highlight a text box widget by changing its background color (`bg`) when the mouse is hovering over it.

```python
from guizero import App, TextBox

def highlight():
    text_box.bg = "lightblue"

def lowlight():
    text_box.bg = "white"

app = App()
text_box = TextBox(app)

# When the mouse enters the TextBox
text_box.when_mouse_enters = highlight
# When the mouse leaves the TextBox
text_box.when_mouse_leaves = lowlight

app.display()
```
