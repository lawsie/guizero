# this is to cater for Python 2, is it really needed? 
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec

# Auto pack or grid position the element
# INTERNAL ONLY
def auto_pack(widget, master, grid, align):

    # If the master widget specifies grid, don't pack, otherwise auto pack
    # You always pack the tk object NOT the guizero object
    if master._layout_manager != "grid":
        widget.tk.pack()
    else:

        # If they failed to specify grid coords
        # Can have 2 values (just coords) or 4 values (coords and col/rowspan)
        if grid is None or type(grid) is not list or (len(grid) != 2 and len(grid) != 4):
            error_format(widget.description + " will not be displayed because it has a missing or " +
            "incorrect grid reference. The format should be grid=[x, y] or grid=[x, y, columnspan, rowspan].")

        else:
            # if we have col span and row span then use them, otherwise default to 1 for both
            columnspan = 1
            rowspan = 1
            # Just check we have more than 2 as we have already checked it's a multiple of two previously
            if len(grid) > 2:
                columnspan = grid[2]
                rowspan = grid[3]
            
            # If no alignment, just place in grid with center align default
            if align is None:
                widget.tk.grid(row=grid[1], column=grid[0], columnspan=columnspan, rowspan=rowspan)
            else:
                # Conversion to child friendly specifications (diags?)
                directions = {"top": "N", "bottom": "S", "left": "W", "right": "E"}
                align_this = "W" # Default to align left if they didn't specify something valid

                try:
                    align_this = directions[align]
                except KeyError:
                    error_format("Invalid align value ('"+ str(align) +"') for " + widget.description +
                    "\nShould be: top, bottom, left or right")

                # Place on grid
                widget.tk.grid(row=grid[1], column=grid[0], columnspan=columnspan, rowspan=rowspan, sticky=align_this)


# Lambda-izer for making it easy to pass arguments with function calls
# without having to know what lambda does
def with_args( func_name, *args):
    return lambda: func_name(*args)

# Gets the number of args a function expects
def no_args_expected(func_name):
    return len(getfullargspec(func_name).args)

# Format errors in a pretty way
def error_format(error_message):
    print("------------------------------------------------------------")
    print("*** GUIZERO WARNING ***" )
    print(error_message)
    print("------------------------------------------------------------")

def deprecated(message):
    print("*** DEPRECATED: " + message)

def convert_color(color):
    # is the color something i.e. not None
    if color:

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
