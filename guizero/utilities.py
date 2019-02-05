# this is to cater for Python 2, is it really needed?
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

from tkinter import PhotoImage, TclError

import sys

class GUIZeroException(Exception):
    pass

# holds details about the configuration guizero is using
class SystemConfig():
    def __init__(self):
        """
        Holds details about the system configuration guizero is using
        """
        self._platform = sys.platform
        if self._platform.startswith("linux"):
            self._platform = "linux"

        if PIL_AVAILABLE:
            self._supported_image_types = ["GIF", "Animated GIF", "BMP", "ICO", "PNG", "JPG", "TIF"]
        else:
            self._supported_image_types = ["GIF", "PNG"]
            if self._platform == "darwin":
                #MacOS only supports GIF with PIL
                self._supported_image_types = ["GIF"]

    @property
    def PIL_available(self):
        """
        Returns `True` if PIL (Python Imaging Library) is available.
        """
        return PIL_AVAILABLE

    @property
    def supported_image_types(self):
        """
        Returns a list of images types supported by this system
        e.g. ('GIF', 'PNG', 'JPG')
        """
        return self._supported_image_types

    @property
    def platform(self):
        """
        Returns the current platform ("linux", "darwin", "win32")
        """
        return self._platform

system_config = SystemConfig()


class GUIZeroImage():
    def __init__(self, image_source, width, height):
        """
        GUIZeroImage manages an "image" for guizero widgets, parsing its
        contents, sizing it accordingly and managing environment.

        :param string image_source:
            The source of the image, a file path, PIL or
            Tk image object.

        :param int width:
            The required width of the image, set to `None`, to keep the
            original image width

        :param int height:
            The required height of the image, set to `None`, to keep the
            original image width.
        """
        self._image_source = image_source
        self._pil_image = None
        self._tk_image = None
        self._tk_frames = []
        self._width = width
        self._height = height
        self._current_frame = 0
        self._animation = False
        self._animation_running = False

        # open the image
        self._setup_image()

    @property
    def image_source(self):
        """
        Returns the original source of the image, be that a file path, PIL or
        Tk image object.
        """
        return self._image_source

    @property
    def tk_image(self):
        """
        Returns the Tk PhotoImage object.
        """
        return self._tk_image

    @property
    def pil_image(self):
        """
        Returns the PIL Image object.
        """
        return self._pil_image

    @property
    def width(self):
        """
        Returns the image width.
        """
        return int(self._width)

    @property
    def height(self):
        """
        Returns the image height.
        """
        return int(self._height)

    @property
    def animation(self):
        """
        Returns `True` if the image contains more than 1 frame (i.e. is an
        animation)
        """
        return self._animation

    @property
    def tk_frames(self):
        """
        Returns a list of frames as Tk PhotoImage objects which make up this
        image.
        """
        return self._tk_frames

    def _setup_image(self):
        try:
            # open image
            self._open_image_source()

            # size image
            self._size_image()

            # open frames
            self._open_image_frames()

        except Exception as e:
            error_text = "Image import error - '{}'\n".format(e)
            error_text += "Check the file path and image type is {}".format("/".join(system_config.supported_image_types))
            raise_error(error_text)

    def _open_image_source(self):
        if system_config.PIL_available:
            if isinstance(self._image_source, str):
                # the source is a string, so try and open as a path
                self._pil_image = Image.open(self._image_source)
                self._tk_image = ImageTk.PhotoImage(self._pil_image)

            elif Image.isImageType(self._image_source):
                # the source is a PIL Image
                self._pil_image = self._image_source
                self._tk_image = ImageTk.PhotoImage(self._pil_image)

            elif isinstance(self._image_source, (PhotoImage, ImageTk.PhotoImage)):
                self._tk_image = self._image_source

            else:
                raise Exception("Image must be a file path, PIL.Image or tkinter.PhotoImage")

        else:
            if isinstance(self._image_source, str):
                self._tk_image = PhotoImage(file=self._image_source)

            elif isinstance(self._image_source, PhotoImage):
                self._tk_image = self._image_source

            else:
                raise Exception("Image must be a file path or tkinter.PhotoImage")

    def _size_image(self):

        # if there is no size, set it to the image width
        if self._width is None:
            self._width = self._tk_image.width()

        if self._height is None:
            self._height = self._tk_image.height()

        # does it need resizing?
        if self._width != self._tk_image.width() or self._height != self._tk_image.height():
            if self._pil_image:
                resized_image = self._pil_image.resize((self._width, self._height), Image.ANTIALIAS)
                self._tk_image = ImageTk.PhotoImage(resized_image)
            else:
                error_format("Image resizing - cannot scale the image as PIL is not available.")

    def _open_image_frames(self):
        if self._pil_image:
            frame_count = 0
            try:
                while True:
                    self._pil_image.seek(frame_count)
                    tk_frame = ImageTk.PhotoImage(self._pil_image.resize((self._width, self._height), Image.ANTIALIAS))

                    try:
                        delay = self._pil_image.info['duration']
                    except:
                        delay = 100

                    self._tk_frames.append((tk_frame, delay))
                    frame_count += 1

            except EOFError as e:
                # end of frames
                pass

            if frame_count > 1:
                self._animation = True


class AnimationPlayer():
    def __init__(self, master, guizero_image, update_image_callback):
        """
        AnimationPlayer manages the playing of a animated gif for guizero
        widgets.

        :param Widget master:
            The widget which is displaying the animation.

        :param GUIZeroImage guizero_image:
            The image object which contains the animation.

        :param function update_image_callback:
            A function which should be called when the Image needs updating.
            The function will be called and passed a reference to the next
            Tk PhotoImage object in the animation.
        """
        self._master = master
        self._guizero_image = guizero_image
        self._update_image_callback = update_image_callback
        self._current_frame = 0
        self._running = False
        self.start()

    @property
    def running(self):
        """
        Returns `True` if the animation is running
        """
        return self._running

    def start(self):
        """
        Starts the animation.
        """
        if not self._running:
            self._running = True
            self._show_frame()

    def stop(self):
        """
        Stops the animation
        """
        self._running = False

    def _show_frame(self):
        if self.running:
            # get the frame
            frame_data = self._guizero_image.tk_frames[self._current_frame]
            frame = frame_data[0]
            delay = frame_data[1]

            # give it to the call back
            self._update_image_callback(frame)

            # increment the frame
            self._current_frame += 1
            if self._current_frame == len(self._guizero_image.tk_frames):
                self._current_frame = 0

            # call again after the delay
            self._master.after(delay, self._show_frame)

# Lambda-izer for making it easy to pass arguments with function calls
# without having to know what lambda does
def with_args( func_name, *args):
    return lambda: func_name(*args)

# Gets the number of args a function expects
def no_args_expected(func_name):
    args = getfullargspec(func_name).args
    if len(args) > 0:
        # if someone names the first arg of a class function to something
        # other than self, this will fail! or if they name the first argument
        # of a non class function to self this will fail!
        if args[0] == "self":
            return len(args) - 1
        else:
            return len(args)
    else:
        return 0

# Format errors in a pretty way
def error_format(message):
    print("------------------------------------------------------------")
    print("*** GUIZERO WARNING ***")
    print(message)
    print("------------------------------------------------------------")

# Raise error in a pretty way
def raise_error(message):
    error_message = "\n------------------------------------------------------------\n"
    error_message += "*** GUIZERO ERROR ***\n"
    error_message += message + "\n"
    error_message += "------------------------------------------------------------\n"
    raise GUIZeroException(error_message)

def deprecated(message):
    print("*** DEPRECATED: " + message)

def convert_color(color):
    """
    Converts a color from "color", (255, 255, 255) or "#ffffff" into a color tk 
    should understand.
    """
    if color is not None:

        # is the color a string
        if isinstance(color, str):
            # strip the color of white space
            color = color.strip()

            # if it starts with a # check it is a valid color
            if color[0] == "#":

                # check its format
                if len(color) != 7:
                    raise ValueError("{} is not a valid # color, it must be in the format #ffffff.".format(color))
                else:
                    # split the color into its hex values
                    hex_colors = (color[1:3], color[3:5], color[5:7])

                    # check hex values are between 00 and ff
                    for hex_color in hex_colors:
                        try:
                            int_color = int(hex_color, 16)
                        except:
                            raise ValueError("{} is not a valid value, it must be hex 00 - ff".format(hex_color))

                        if not (0 <= int_color <= 255):
                            raise ValueError("{} is not a valid color value, it must be 00 - ff".format(hex_color))

        # if the color is not a string, try and convert it
        else:
            # get the number of colors and check it is iterable
            try:
                no_of_colors = len(color)
            except:
                raise ValueError("A color must be a list or tuple of 3 values (red, green, blue)")

            if no_of_colors != 3:
                raise ValueError("A color must contain 3 values (red, green, blue)")

            # check the color values are between 0 and 255
            for c in color:
                if not (0 <= c <= 255):
                    raise ValueError("{} is not a valid color value, it must be 0 - 255")

            # convert to #ffffff format
            color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

    return color
