## Images

Widgets such as [Picture](picture.md) and [PushButton](pushbutton.md) allow you to use images in your GUI.

```python
from guizero import App, Picture
app = App()
picture = Picture(app, image="test.gif")
app.display()
```

The types of image (GIF, JPG, PNG, etc) supported depend on how you [installed guizero](index.md) and the setup of your computer.

### Supported files types

All systems support the `GIF` file type.

Windows and Linux also support `PNG` files.

If you [installed the addition image features](index.md#additional-features-install) using `pip` it will also have installed `PIL` (Python Imaging Library) and you will be able use the majority of commonly used image types.

guizero will tell you what file types are supported on your computer using the following code:

```python
from guizero import system_config
print(system_config.supported_image_types)
```

| Operating System | PIL NOT available | PIL available                              |
|------------------|-------------------|--------------------------------------------|
| Windows          | GIF, PNG          | GIF, Animated GIF, BMP, ICO, PNG, JPG, TIF |
| MacOS            | GIF               | GIF, Animated GIF, BMP, ICO, PNG, JPG, TIF |
| Linux            | GIF, PNG          | GIF, Animated GIF, BMP, ICO, PNG, JPG, TIF |
| Raspbian         | GIF, PNG          | GIF, Animated GIF, BMP, ICO, PNG, JPG, TIF |

### Resizing

When the size of a widget is changed the image will be changed to fit the widget. If the additional image features were installed and `PIL` is available, the image will be scaled correctly, if not the image will be cropped.

### Animated GIFs

If `PIL` is installed guizero supports displaying animated GIFs, if not, the GIF will be displayed as a static image.
