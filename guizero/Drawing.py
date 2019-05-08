from tkinter import Canvas, ALL
from tkinter.font import Font
from . import utilities as utils
from .base import Widget
from .event import EventManager

class Drawing(Widget):

    def __init__(
        self, 
        master, 
        width=100, 
        height=100, 
        grid=None, 
        align=None, 
        visible=True, 
        enabled=None):
        """
        Creates a Drawing

        :param Container master:
            The Container (App, Box, etc) the Drawing will belong too.

        :param int width:
            The starting width of the widget. Defaults to `None` and will auto
            size.

        :param int height:
            The starting height of the widget. Defaults to `None` and will auto
            size.
        
        :param List grid:
            Grid co-ordinates for the widget, required if the master layout
            is 'grid', defaults to `None`.

        :param string align:
            How to align the widget within the container, defaults to None.

        :param bool visible:
            If the widget should be visible, defaults to `True`.

        :param bool enabled:
            If the widget should be enabled, defaults to `None`. If `None`
            the value is inherited from the master.

        """

        # list to hold references to images, otherwise tk destroys them
        self._images = {}

        description = "[Drawing] object"

        tk = Canvas(master.tk, height=100, width=100, bd=0, highlightthickness=0)

        super(Drawing, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

    def line(self, x1, y1, x2, y2, color="black", width=1):
        """
        Draws a line between 2 points

        :param int x1:
            The x position of the starting point.

        :param int y1:
            The y position of the starting point.

        :param int x2:
            The x position of the end point.

        :param int y2:
            The y position of the end point.

        :param str color:
            The color of the line. Defaults to `"black"`.

        :param int width:
            The width of the line. Defaults to `1`.

        :return:
            The id of the line.
        """
        return self.tk.create_line(
            x1, y1, x2, y2, 
            width = width,
            fill = "" if color is None else utils.convert_color(color)
            )

    def oval(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        """
        Draws an oval between 2 points

        :param int x1:
            The x position of the starting point.

        :param int y1:
            The y position of the starting point.

        :param int x2:
            The x position of the end point.

        :param int y2:
            The y position of the end point.

        :param str color:
            The color of the shape. Defaults to `"black"`.

        :param int outline:
            `0` or `False` is no outline. `True` or value > 1 sets an outline. Defaults to `False`.

        :param str outline_color:
            The color of the outline. Defaults to `"black"`.

        :return:
            The id of the shape.
        """
        return self.tk.create_oval(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def rectangle(self, x1, y1, x2, y2, color="black", outline=False, outline_color="black"):
        """
        Draws a rectangle between 2 points

        :param int x1:
            The x position of the starting point.

        :param int y1:
            The y position of the starting point.

        :param int x2:
            The x position of the end point.

        :param int y2:
            The y position of the end point.

        :param str color:
            The color of the shape. Defaults to `"black"`.

        :param int outline:
            `0` or `False` is no outline. `True` or value > 1 sets an outline. Defaults to `False`.

        :param str outline_color:
            The color of the outline. Defaults to `"black"`.

        :return:
            The id of the shape.
        """
        return self.tk.create_rectangle(
            x1, y1, x2, y2, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def polygon(self, *coords, color="black", outline=False, outline_color="black"):
        """
        Draws a polygon from an list of co-ordinates

        :param int *coords:
            Pairs of x and y positions which make up the polygon.

        :param str color:
            The color of the shape. Defaults to `"black"`.

        :param int outline:
            `0` or `False` is no outline. `True` or value > 1 sets an outline. Defaults to `False`.

        :param str outline_color:
            The color of the outline. Defaults to `"black"`.

        :return:
            The id of the shape.
        """
        return self.tk.create_polygon(
            *coords, 
            outline = utils.convert_color(outline_color) if outline else "",
            width = int(outline),
            fill = "" if color is None else utils.convert_color(color)
            )

    def triangle(self, x1, y1, x2, y2, x3, y3, color="black", outline=False, outline_color="black"):
        """
        Draws a triangle between 3 points

        :param int x1:
            The x position of the starting point.

        :param int y1:
            The y position of the starting point.

        :param int x2:
            The x position of the middle point.

        :param int y2:
            The y position of the middle point.

        :param int x3:
            The x position of the end point.

        :param int y3:
            The y position of the end point.

        :param str color:
            The color of the shape. Defaults to `"black"`.

        :param int outline:
            `0` or `False` is no outline. `True` or value > 1 sets an outline. Defaults to `False`.

        :param str outline_color:
            The color of the outline. Defaults to `"black"`.

        :return:
            The id of the shape.
        """
        return self.polygon(
            x1, y1, x2, y2, x3, y3, 
            color=color, 
            outline=outline, 
            outline_color=outline_color)

    def image(self, x, y, image, width=None, height=None):
        """
        Inserts an image into the drawing, position by its top-left corner.
        
        :param int x:
            The x position to insert the image.

        :param int y:
            The y position to insert the image.

        :param str image:
            The file path or a PhotoImage or PIL.Image object.

        :param str width:
            The width to scale the image too, setting to `None` will use the
            actual width of the Image. Default to `None`.

        :param str height:
            The width to scale the image too, setting to `None` will use the 
            actual height of the Image. Default to `None`.

        :return:
            The id of the image.
        """
        # load the image and add to the dict (otherwise tk destroys the reference to them!)
        _image = utils.GUIZeroImage(image, width, height)
        id = self.tk.create_image(x, y, image=_image.tk_image, anchor="nw")
        self._images[id] = _image
        return id
    
    def text(self, x, y, text, color="black", font=None, size=None, max_width=None):
        """
        Inserts text into the drawing, position by its top-left corner.
        
        :param int x:
            The x position of the text.

        :param int y:
            The x position of the text.

        :param str color:
            The color of the text. Defaults to `"black"`.

        :param str font:
            The font to use. Defaults to `None` and will use the system
            default font.

        :param int size:
            The size of the text. Defaults to `None` and will use the system
            default font size.

        :param int max_width:
            Maximum line length. Lines longer than this value are wrapped. 
            Default is `None` (no wrapping).
        """
        # create the font
        if size is None:
            f = Font(self.tk, family=font)
        else:
            f = Font(self.tk, family=font, size=size)
        
        return self.tk.create_text(
            x, y, 
            text=text,
            fill = "" if color is None else utils.convert_color(color),
            font=f,
            width=max_width,
            anchor="nw")

    def delete(self, id):
        """
        Deletes an "object" (line, triangle, image, etc) from the drawing.

        :param int id:
            The id of the object.
        """
        if id in self._images.keys():
            del self._images[id]
        self.tk.delete(id)

    def clear(self):
        """
        Clears the drawing.
        """
        self._images.clear()
        self.tk.delete(ALL)
