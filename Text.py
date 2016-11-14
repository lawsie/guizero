try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

import utilities as utils
    
class Text(Label):

    def __init__(self, master, text="", size=12, color="black", font="Helvetica", grid=None, align=None):


        # Description of this object (for friendly error messages)
        self.description = "[Text] object with text \"" + str(text) + "\""

        # Save some of the config
        self.current_size = size
        self.current_color = color
        self.current_font = font

        # Create a Tkinter String variable controlling the text within the label
        self.string_var = StringVar()
        self.string_var.set( str(text) )

        # Attempt to instantiate the object and raise an error if failed
        try:
            super().__init__(master)
        except AttributeError:
            utils.error_format( self.description + "\n" +
            "The first argument was a " + str(type(master)) +". First argument must be [App] or [Box]")

        # Initial config on setup       
        self.config(textvariable=self.string_var, fg=color, font=(font, size))
        
        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)


    # Clear text (set to empty string)
    def clear(self):
        self.string_var.set("")
        
    # Returns the text
    def get(self):
        return self.string_var.get()

    # Sets the text
    def set(self, text):
        self.string_var.set(text)

    # Sets the text colour
    def color(self, color):
        self.config(fg=color)

    # Set the font 
    def font_face(self, font):
        self.current_font = font
        self.config(font=(self.current_font, self.current_size))

    # Set the font size
    def font_size(self, size):
        self.current_size = size
        self.config(font=(self.current_font, self.current_size))

    # Append to the StringVar controlling this text
    def append(self, text):
        self.string_var.set( self.string_var.get() + str(text) )

