# How to...

This section aims to explain features that are common to all classes of guizero.

## Specifying parameters

When first creating an object, you can specify parameters (the properties you want the object to have) in two possible ways:

### Option 1 - in order
Specify the parameters in the *exact* order given in the table on the documentation page. You do not have to specify all of the optional parameters, but you must specify them in order and not miss any out.

For example if the parameters available were **a, b, c, d, e**

- Specifying **a, b, c** is valid
- Specifying **a, b, d, e** is not valid as you have missed out c but still specified later parameters

Here is an example of code with parameters specified in this way

```python
app = App("Title of my app")
input_box = TextBox(app, "Type here")
```

This way will probably be most useful for younger children where programs are not likely to need complex configuration options.

### Option 2 - as keyword arguments
Compulsory parameters should always be specified in the exact order given in the documentation, for example the `master` parameter is a compulsory first parameter for all widgets.

If you only want to specify some of the *optional* parameters, you can specify them after the compulsory parameters in any order, using the format `parameter=value`.

In this example the compulsory parameter `app` has been specified first, followed by the optional `width` parameter.

```python
app = App()
input_box = TextBox(app, width=20)
```
