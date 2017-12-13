# MenuBar

(Extends the `Menu` class from `tkinter`)

### Purpose
Display a menu at the top of the screen, each option having a submenu

```
class guizero.MenuBar(master, toplevel, options)
```

### Create a MenuBar object

Create a basic MenuBar object like this:

```python
from guizero import App, MenuBar
def file_function():
    print("File option")

def edit_function():
    print("Edit option")

app = App()
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", file_function], ["File option 2", file_function] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                  ])
app.display()

```

The `toplevel` parameter should be a list of options you wish to display on the menu. In this example the toplevel options are File and Edit:

![Top level menu on Windows](images/toplevel_windows.png)

The options parameter should be a 3D List containing lists of submenu items, which are themselves lists. The elements in the list correspond to the elements in the `toplevel` list, so the first list of submenu items provided in `options` will be the submenu for the first menu heading provided in `toplevel` and so on.

The menu item sub-sublists within `options` should contain pairs consisting of the text to display on the menu and the function to call when that option is selected. In this example, the text "File option 1" is displayed and the function `file_function` is called if this option is clicked on.

```python
["File option 1", file_function]
```
Here is what this code looks like on Windows:

![MenuBar on Windows](images/menubar_windows.png)


When creating a MenuBar object, you must specify the following parameters. (More information about how to specify parameters can be found in the ['How to...'](./howto/) section.)

| Parameter | Takes | Default | Compulsory | Description                         |
| --------- | --------- | ------- | ---------- | -------------------------|
| master    | App   | - | Yes       | The container to which this widget belongs
| toplevel   | List    | -  | Yes         | A list of top level menu items |
| options | 3D List | - | Yes   | A list of submenus, with each submenu being a list of options and each option being a text/command pair. See notes above for more details. |

The MenuBar is never displayed on a grid so there are no grid or alignment parameters.


### Methods

There are no methods for the MenuBar object

### Examples

**Creating a MenuBar**

The simplest way to create a MenuBar object is as follows:

```python
from guizero import App, MenuBar
def file_function():
    print("File option")

def edit_function():
    print("Edit option")

app = App()
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", file_function], ["File option 2", file_function] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                  ])
app.display()
```
