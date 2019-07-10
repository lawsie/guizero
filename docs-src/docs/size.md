## Sizes

You can set the `width` and `height` of widgets in guizero.

Widgets are sized by either pixels or characters depending on the widget and what it contains.

Some widgets size can also be set to `"fill"` where it will use up all of the available space.

``` python
from guizero import App, PushButton, Slider, ListBox

app = App()

# A PushButton's size is noted in characters
button = PushButton(app, width=30, height=5)

# A Slider's size is noted in pixels
slider = Slider(app, width=300, height=30)

# Some widgets such as ListBox can also be told to fill all the available space
listbox = ListBox(app, width="fill", height="fill")

app.display()
```

| Widget                                 | Characters or Pixels | Fill | Notes                                                                  |
|----------------------------------------|----------------------|------|------------------------------------------------------------------------|
| [Box](box.md)                          | Pixels               | Yes  | If a Box is sized in Pixels, both width and height must be specified.  |
| [ButtonGroup](buttongroup.md)          | Characters           | Yes  | The height of a ButtonGroup must divide by the number of buttons in it |
| [CheckBox](checkbox.md)                | Characters           | Yes  |                                                                        |
| [Combo](combo.md)                      | Characters           | Yes  |                                                                        |
| [ListBox](listbox.md)                  | Pixels               | Yes  |                                                                        |
| [Picture](picture.md)                  | Pixels               | No   | See [Images](images.md) for more information                           |
| [PushButton](pushbutton.md)            | Characters           | Yes  |                                                                        |
| [PushButton](pushbutton.md) with image | Pixels               | No   | PushButton's which have images are sized in pixels                     |
| [Slider](slider.md)                    | Pixels               | Yes  |                                                                        |
| [Text](text.md)                        | Characters           | Yes  |                                                                        |
| [TextBox](textbox.md)                  | Characters           | Yes  | Only a TextBox's width can be set                                      |
| [Waffle](waffle.md)                    | Pixels               | No   |                                                                        |
