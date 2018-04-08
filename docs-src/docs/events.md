## Events

Custom events can be added to guizero widgets to call functions when the user takes the following actions:
- `when_clicked`
- `when_left_button_pressed`
- `when_left_button_released`
- `when_right_button_pressed`
- `when_right_button_released`
- `when_key_pressed`
- `when_key_released`
- `when_mouse_enters`
- `when_mouse_leaves`
- `when_mouse_dragged`

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

# when the mouse enters the textbox
text_box.when_mouse_enters = highlight
# when the mouse leaves the textbox
text_box.when_mouse_leaves = lowlight

app.display()
```

_Warning - events are currently experimental and issues maybe experienced_.