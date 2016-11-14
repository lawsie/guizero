## guizero

# Mission statement
The aim of guizero is to make the process of creating simple GUIs quick, accessible and understandable for children.

# Aims
* Works with standard Python GUI library (and no need to install other libraries)
* Abstracts away details such as Tkinter StringVar() objects
* Accessible widget naming system to help children to build up a mental model
* Flexible enough to be used for projects up to A-Level standard, accessible to primary school children
* Comprehensive and accessible documentation with examples
* Helpful error messages

# Included at the moment
* App - (Tk) The main tkinter window. Layout defaults to pack but can be specified as grid. Pack components self-pack, grid components are packed via providing a list argument to the object's constructor with the desired position on the grid.
* Box - (Frame) A way of grouping components
* Combo - (OptionMenu) A combo box with methods to get option, set option, select default, add option and clear
* MenuBar - (Menu with self instantiating sub-Menu) Create a top level menu with submenus (one level) by passing lists
* Picture - (Label) Display a gif
* Slider - (Scale) Display a slider control which can call a function when its value is changed
* Text - (Label) Display some text, with methods to clear, get contents, set, append and alter font, size and colour
* TextBox - (Entry) A text box with methods to clear, get contents, set and append
* ZeroButton - (Button) A button which can display text or a (gif) image and calls a function
* utilities - Some functions to help the GUI auto pack itself, to allow callbacks to be passed arguments and to format errors nicely

# To do list
* Add CheckBox 
* Add RadioButton
* Add Alert (pop up message)
* Add docstrings
* Work out why you have to import tkinter separately at the start of each class file(?!)
