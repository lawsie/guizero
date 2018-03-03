## Sizes

You can set the `width` and `height` of widgets in guizero.

Widgets are sized by pixels or characters depending on the widget and what it contains.

``` python
from guizero import App, PushButton, Slide
app = App()

# a PushButton's size is noted in characters
button = PushButton(app)
button.width = 30
button.height = 30

# a Slider's size is noted in pixels
slider = Slider(app)
slider.width = 300
slider.height = 30  
```

| Widget        | Characters or Pixels | Notes |
| ------------- | ----------- | ------------- |
| Box           | Pixels      | The size only takes affect if the Box is empty, if the Box contains any widgets it will size to the widgets inside it |
| ButtonGroup   | Characters  | The height of a ButtonGroup must divide by the number of buttons in it |
| CheckBox      | Characters  | |
| Combo         | Characters  | |
| Picture       | Pixels      | The image wont scale to the size of the Picture |
| PushButton    | Characters  | PushButton's are sized in Characters, unless they contain an icon in which case they are sized in Pixels |
| Slider        | Pixels      | |
| Text          | Characters  | |
| TextBox       | Characters  | Only a TextBox's width can be set |
| Waffle        | Pixels      | |
