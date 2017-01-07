try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

from . import utilities as utils

class App(Tk):

    def __init__(self, title="GUIzero", width=500, height=500, layout="auto", bgcolor=None):

        try:
            super().__init__()
        except:            
            utils.error_format("Failed to initialise [App] object")

        # Initial setup
        self.title( str(title) )
        self.geometry(str(width)+"x"+str(height))
        self.layout_manager = layout  		# Only behaves differently if equals "grid"

        if bgcolor is not None:
            self.configure(background=str(bgcolor))
    
    
    # Alias of mainloop with friendlier name
    def display(self):
        super().mainloop()

    # Set the title of the window
    def set_title(self, title):
        self.title( str(title) )

    # do `command` on window close instruction
    def on_close(self, command):
        super().wm_protocol("WM_DELETE_WINDOW", command)

    # Method destroy() is already in tkinter, will close app window

    # Change the background colour
    def bgcolor(self, bgcolor):
        self.configure(background=str(bgcolor))