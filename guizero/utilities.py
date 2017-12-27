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

# Format errors in a pretty way
def error_format(error_message):
    print("------------------------------------------------------------")
    print("*** GUIZERO WARNING ***" )
    print(error_message)
    print("------------------------------------------------------------")

def deprecated(message):
    print("*** DEPRECATED: " + message)
