__name__ = "guizero"
__package__ = "guizero"
__version__ = '1.1.0'
__author__ = "Laura Sach"

from sys import exit
try:
    from tkinter import Tk
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")
    exit(1)

from . import utilities as utils
from .utilities import system_config
from .dialog import *

from .App import App
from .Box import Box
from .ButtonGroup import ButtonGroup
from .CheckBox import CheckBox
from .Combo import Combo
from .Drawing import Drawing
from .ListBox import ListBox
from .MenuBar import MenuBar
from .Picture import Picture
from .PushButton import PushButton
from .RadioButton import RadioButton
from .Slider import Slider
from .Text import Text
from .TextBox import TextBox
from .PushButton import PushButton
from .Waffle import Waffle
from .Window import Window
