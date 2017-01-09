try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils
from .guizerocontroleventcore import GuiZeroControlEventCore


class Picture(Label, GuiZeroControlEventCore):

    def __init__(self, master, image, grid=None, align=None):


        try:
            img = PhotoImage(file=image)                      
        except:
            utils.error_format("Image import error - image must be a gif, check correct path")

        self.image = img  

        # Description of this object (for friendly error messages)
        self.description = "[Picture] object \"" + str(self.image) + "\""

        # Attempt to instantiate the object and raise an error if failed
        try:
            super().__init__(master)
        except AttributeError:
            error_format(self.description + "\n" +
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")
            

        # Initial config on setup       
        self.config(image=self.image)
        
        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)

    # Sets the image to something new
    def set(self, image):
        try:
            img = PhotoImage(file=image) 
            self.image = img  
            self.config(image=self.image)              
        except:
            utils.error_format("Image import error - image must be a gif, check correct path")
        

   
