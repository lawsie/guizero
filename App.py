try:
    from tkinter import *
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")

import utilities as utils
    
class App(Tk):

    def __init__(self, manager="auto", title="GuiZero",  height=500, width=500):

        try:
            super().__init__()
        except:            
            utils.error_format("Failed to initialise [App] object")

        # Initial setup
        self.title( str(title) )
        self.geometry(str(height)+"x"+str(width))
        self.layout_manager = manager  		# Only behaves differently if equals "grid"
    
    
    # Alias of mainloop with friendlier name
    def display(self):
        super().mainloop()

    # Set the title of the window
    def set_title(self, title):
        self.title( str(title) )

   