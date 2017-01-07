# Text

(Extends the `Label` class from `tkinter`)

### Purpose
Display non editable text in your app, such as for titles, labels and instructions.

```
class guizero.Text(master, text="", size=12, color="black", font="Helvetica", grid=None, align="left")
```

### Create a Text object

Create a basic Text object like this:

```python
app = App()
text = Text(app, "Hello World")
app.display()
```


When creating a Text object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Data type | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| text   | string    | ""  | No         | The text you want to display |
| size   | int    | 12     | No         | The font size of the text |
| color   | string     | black     | No         | The colour of the text. Accepts some colour strings (e.g. `red`) and colours specified in hex format (e.g. `#0099ff`)  |
| font   | string     | "Helvetica"     | No         | The font face that the text will be displayed in. Availability of fonts depends on which fonts are installed locally. |
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | "left"     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |


### Methods

You can call the following methods on your Text object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| append(text)  | text (string) | -          | Adds the provided `text` to the end of the current text within the object |
| clear()   | -             | -          | Clears the text            |
| color(color) | color (string) | -      | Sets the colour of the text to the `color` provided. This can be a defined colour (e.g. "blue") or a hex format rgb colour (e.g. "#ff0000") |
| font_face(font) | font (string) | - | Sets the font face to the `font` provided |
| font_size(size) | size (int) | - |  Sets the font size to the `size` provided |
| get() | - | string |  Returns a string containing the text from the object |
| set(text) | text (string) | - |  Sets the text within the object to the `text` provided |

Call a method like this:

```python
app = App()
writing = Text(app, text="Hello world", color="red")

# Call the font_size() method
writing.font_size(20)   
```

### Examples

**Creating text**

The simplest way to create a text object is as follows:

```python
app = App()
mytext = Text(app, "Hello world")
app.display()
```
