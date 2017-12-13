# Waffle

(Extends the `Frame` class from `tkinter`)

### Purpose
Display an n*n grid of squares with custom dimensions and padding

```
class guizero.Waffle(master, height=3, width=3, dim=20, pad=5, color="white", dotty=False, remember=False, grid=None, align=None):    	
```

### Create a Waffle object

Create a basic Waffle object like this:

```python
app = App()
my_waffle = Waffle(app)
app.display()
```

The above code looks like this on Windows:
![Waffle on Windows](images/waffle_windows.png)


When creating a Waffle object, you can specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Takes     | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App or Box| -       | Yes        | The container to which this widget belongs |
| height    | int       | 3       | No         | How many pixels high the waffle is |
| width     | int       | 3       | No         | How many pixels wide the waffle is |
| dim       | int       | 20      | No         | How large one of the pixels on the waffle is |
| pad       | int       | 5       | No         | How much space is between the pixels on the waffle |
| color     | string    | "white" | No         | The starting colour of all pixels on the waffle |
| dotty     | boolean   | False   | No         | Whether the pixels display as dots/circles (True) or squares (False) |
| remember  | boolean   | False   | No         | Whether the Waffle keeps an internal list of the colour of each pixel (True) or not (False). Use this if you want to use get_pixel() and get_all() methods. |
| grid      | List [int, int]     | None       | No         | `[x,y]` coordinates of this widget. This parameter is only required if the `master` object has a grid layout. |
| align     | string     | None   | No         | Alignment of this widget within its grid location. Possible values: `"top"`, `"bottom"`, `"left"`, `"right"`. This parameter is only required if the `master` object has a grid layout.  |



### Methods

You can call the following methods on your Waffle object

| Method        | Takes     | Returns    | Description                |
| ------------- | ------------- | ---------- | -------------------------- |
| set_all(color)     | color (string) | -          | Sets all pixels to the specified colour (allows hex code e.g. #0099ff or colour name e.g. "red") |
| set_pixel(x, y, color)   | x (int), y (int), color (string)     | -         | Sets the pixel at the specified coordinates to the specified colour. 0,0 is the top left of the grid.  |
| get_all()     | - | List | IMPORTANT: To use this function, you must set remember=True when you create the Waffle. Returns the pixel colours in the grid as a 2D list. |
| get_pixel(x, y)| x (int), y (int) | string |  IMPORTANT: To use this function, you must set remember=True when you create the Waffle. Returns the colour of the pixel at the specified coordinates. 0,0 is the top left of the grid. |

### Examples

**Creating a Waffle**

The simplest way to create a Waffle object is as follows:

```python
app = App()
my_waffle = Waffle(app)
app.display()
```

**Waffle with a memory**

A Waffle can be given a memory, so that it remembers the colour of each pixel within it.

```python
from guizero import App, Waffle

app = App()

# Set the waffle to have a memory
my_waffle = Waffle(app, remember=True)

my_waffle.set_pixel(2, 1, "red")

# Now your waffle will remember what colour each pixel is!
print(my_waffle.get_pixel(2,1))

# Even the ones auto-set at the start (which are white by default)
print(my_waffle.get_pixel(1,1))

app.display()

```
