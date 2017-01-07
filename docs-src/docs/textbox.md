# TextBox

(Extends the `Entry` class from `tkinter`)

### Purpose
Display a text box which the user can type in

```
class guizero.TextBox(master, text="", width=10, grid=None, align=None)
```

### Create a TextBox object

Create a basic TextBox object like this:

```python
app = App()
input_box = TextBox(app)
app.display()
```


When creating a Text object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)
 
| Parameter | Data type | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box   | - | Yes       | The container to which this widget belongs
| text   | string    | ""  | No         | Any text you wish to be pre-filled in the text box |
| width   | int    | 10     | No         | The width of the text box|
| grid   | List [int, int]   | None     | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align   | string     | None     | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |


### Methods

You can call the following methods on your TextBox object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| append(text)  | text (string) | -          | Adds the provided `text` to the end of the current text within the text box |
| clear()   | -             | -          | Clears the textbox            |
| get() | - | string |  Returns a string containing current contents of the textbox |
| set(text) | text (string) | - |  Sets the text within the text box to the `text` provided |

Call a method like this:

```python
app = App()
input_box = TextBox(app, "Type here")

# Call the clear() method
input_box.clear()  
```

### Examples

**Creating a TextBox**

The simplest way to create a TextBox  object is as follows:

```python
app = App()
input_box = TextBox(app, "Type here")
app.display()
```
